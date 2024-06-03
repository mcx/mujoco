# Copyright 2024 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List, Optional, Tuple
import pprint

import mujoco

import mujoco.usd.utils as utils_component
import mujoco.usd.shapes as shapes_component

import numpy as np

# TODO: b/288149332 - Remove once USD Python Binding works well with pytype.
# pytype: disable=module-attr
from open3d import open3d as o3d
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdLux
from pxr import UsdShade
from pxr import Vt

class USDObject(ABC):
  """ Abstract interface for all USD objects including meshes and primitives

  Subclasses must implement:

  * `_get_uv_geometry(self)`: gets the nessecary UV information to wrap a texture 
     around an object in USD. Each subclass implements their own method to getting
     UV information as different objects are contructed in different ways.

  * `_get_mesh_geometry(self)`: gets the mesh geometry of an object in the scene.
  """

  def __init__(
      self,
      stage: Usd.Stage,
      geom: mujoco.MjvGeom,
      obj_name: str,
      rgba: np.ndarray = np.array([1, 1, 1, 1]),
      texture_file: Optional[str] = None,
  ):
    self.stage = stage
    self.geom = geom
    self.obj_name = obj_name
    self.rgba = rgba
    self.texture_file = texture_file

    self.xform_path = f"/World/Mesh_Xform_{obj_name}"
    self.usd_xform = UsdGeom.Xform.Define(stage, self.xform_path)

    # defining ops required by update function
    self.transform_op = self.usd_xform.AddTransformOp()
    self.scale_op = self.usd_xform.AddScaleOp()

    self.last_visible_frame = -2 # not an arbitary value, forces difference greater than 1 for visibility on 0th frame

  @abstractmethod
  def _get_uv_geometry(self):
    """Gets UV information for an object in the scene"""
    raise NotImplementedError
  
  @abstractmethod
  def _get_mesh_geometry(self):
    """Gets structure of an object in the scene"""
    raise NotImplementedError

  def attach_image_material(self, usd_mesh):
    """Attaches an image texture to a material for a USD object"""
    mtl_path = Sdf.Path(f"/World/_materials/Material_{self.obj_name}")
    mtl = UsdShade.Material.Define(self.stage, mtl_path)

    bsdf_shader = UsdShade.Shader.Define(
        self.stage, mtl_path.AppendPath("Principled_BSDF")
    )
    image_shader = UsdShade.Shader.Define(
        self.stage, mtl_path.AppendPath("Image_Texture")
    )
    uvmap_shader = UsdShade.Shader.Define(
        self.stage, mtl_path.AppendPath("uvmap")
    )

    # setting the bsdf shader attributes
    bsdf_shader.CreateIdAttr("UsdPreviewSurface")
    bsdf_shader.CreateInput(
        "diffuseColor", Sdf.ValueTypeNames.Color3f
    ).ConnectToSource(image_shader.ConnectableAPI(), "rgb")
    bsdf_shader.CreateInput("opacity", Sdf.ValueTypeNames.Float).Set(
        float(self.rgba[-1])
    )
    bsdf_shader.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(
        self.geom.shininess
    )
    bsdf_shader.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(
        1.0 - self.geom.shininess
    )

    mtl.CreateSurfaceOutput().ConnectToSource(
        bsdf_shader.ConnectableAPI(), "surface"
    )

    # setting the image texture attributes
    image_shader.CreateIdAttr("UsdUVTexture")
    image_shader.CreateInput("file", Sdf.ValueTypeNames.Asset).Set(
        self.texture_file
    )
    image_shader.CreateInput(
        "sourceColorSpace", Sdf.ValueTypeNames.Token
    ).Set("sRGB")
    image_shader.CreateInput("wrapS", Sdf.ValueTypeNames.Token).Set("repeat")
    image_shader.CreateInput("wrapT", Sdf.ValueTypeNames.Token).Set("repeat")
    image_shader.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(
        uvmap_shader.ConnectableAPI(), "result"
    )
    image_shader.CreateOutput("rgb", Sdf.ValueTypeNames.Float3)

    # setting uvmap shader attributes
    uvmap_shader.CreateIdAttr("UsdPrimvarReader_float2")
    uvmap_shader.CreateInput("varname", Sdf.ValueTypeNames.Token).Set("UVMap")
    uvmap_shader.CreateOutput("results", Sdf.ValueTypeNames.Float2)

    mtl.CreateSurfaceOutput().ConnectToSource(
        bsdf_shader.ConnectableAPI(), "surface"
    )

    usd_mesh.GetPrim().ApplyAPI(UsdShade.MaterialBindingAPI)
    UsdShade.MaterialBindingAPI(usd_mesh).Bind(mtl)

  def attach_solid_material(self, usd_mesh):
    """Attaches an solid texture to a material for a USD object"""
    mtl_path = Sdf.Path(f"/World/_materials/Material_{self.obj_name}")
    mtl = UsdShade.Material.Define(self.stage, mtl_path)

    bsdf_shader = UsdShade.Shader.Define(
        self.stage, mtl_path.AppendPath("Principled_BSDF")
    )

    # settings the bsdf shader attributes
    bsdf_shader.CreateIdAttr("UsdPreviewSurface")

    bsdf_shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(
        tuple(self.rgba[0:3])
    )
    bsdf_shader.CreateInput("opacity", Sdf.ValueTypeNames.Float).Set(
        float(self.rgba[-1])
    )
    bsdf_shader.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(
        self.geom.shininess
    )
    bsdf_shader.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(
        1.0 - self.geom.shininess
    )

    mtl.CreateSurfaceOutput().ConnectToSource(
        bsdf_shader.ConnectableAPI(), "surface"
    )

    usd_mesh.GetPrim().ApplyAPI(UsdShade.MaterialBindingAPI)
    UsdShade.MaterialBindingAPI(usd_mesh).Bind(mtl)

  def _set_refinement_properties(self, usd_prim, scheme="none"):
    usd_prim.GetAttribute("subdivisionScheme").Set(scheme)

  def update(self, pos: np.ndarray, mat: np.ndarray, visible: bool, frame: int, scale: Optional[np.ndarray] = None):
    """Updates the position and orientation of an object in the scene for a given frame"""
    transformation_mat = utils_component.create_transform_matrix(
        rotation_matrix=mat, translation_vector=pos
    ).T
    self.transform_op.Set(Gf.Matrix4d(transformation_mat.tolist()), frame)
    
    if visible and frame - self.last_visible_frame > 1:
      # non consecutive visible frames
      self.update_visibility(False, max(0, self.last_visible_frame))
      self.update_visibility(True, frame)

    if visible:
      self.last_visible_frame = frame

    if scale is not None:
      self.update_scale(scale, frame)

  def update_visibility(self, visible: bool, frame: int):
    """Updates the visibility of an object in a scene for a given frame"""
    visibility_setting = "inherited" if visible else "invisible"
    self.usd_xform.GetVisibilityAttr().Set(visibility_setting, frame)

  def update_scale(self, scale: np.ndarray, frame: int):
    """Updates the scale of an object in the scene for a given frame"""
    self.scale_op.Set(Gf.Vec3f(scale.tolist()), frame)

class USDMesh(USDObject):

  def __init__(
      self,
      stage: Usd.Stage,
      model: mujoco.MjModel,
      geom: mujoco.MjvGeom,
      obj_name: str,
      dataid: int,
      rgba: np.ndarray = np.array([1, 1, 1, 1]),
      texture_file: Optional[str] = None,
  ):
    super().__init__(stage,
                     geom,
                     obj_name,
                     rgba,
                     texture_file)

    self.model = model
    self.dataid = dataid

    mesh_path = f"{self.xform_path}/Mesh_{obj_name}"
    self.usd_mesh = UsdGeom.Mesh.Define(stage, mesh_path)
    self.usd_prim = stage.GetPrimAtPath(mesh_path)

    # setting mesh structure properties
    mesh_vert, mesh_face, mesh_facenum = self._get_mesh_geometry()
    self.usd_mesh.GetPointsAttr().Set(mesh_vert)
    self.usd_mesh.GetFaceVertexCountsAttr().Set(
        [3 for _ in range(mesh_facenum)]
    )
    self.usd_mesh.GetFaceVertexIndicesAttr().Set(mesh_face)

    # setting mesh uv properties
    mesh_texcoord, mesh_facetexcoord = self._get_uv_geometry()
    self.texcoords = UsdGeom.PrimvarsAPI(self.usd_mesh).CreatePrimvar(
        "UVMap", Sdf.ValueTypeNames.TexCoord2fArray, UsdGeom.Tokens.faceVarying
    )
    self.texcoords.Set(mesh_texcoord)
    self.texcoords.SetIndices(Vt.IntArray(mesh_facetexcoord.tolist()))

    if self.texture_file:
      self.attach_image_material(self.usd_mesh)
    else:
      self.attach_solid_material(self.usd_mesh)

  def get_facetexcoord_ranges(self, nmesh, arr):
    facetexcoords_ranges = [0]
    running_sum = 0
    for i in range(nmesh):
      running_sum += arr[i] * 3
      facetexcoords_ranges.append(running_sum)
    return facetexcoords_ranges

  def _get_uv_geometry(self):
    mesh_texcoord_adr_from = self.model.mesh_texcoordadr[self.dataid]
    mesh_texcoord_adr_to = (
        self.model.mesh_texcoordadr[self.dataid + 1]
        if self.dataid < self.model.nmesh - 1
        else len(self.model.mesh_texcoord)
    )
    mesh_texcoord = self.model.mesh_texcoord[
        mesh_texcoord_adr_from:mesh_texcoord_adr_to
    ]

    mesh_facetexcoord_ranges = self.get_facetexcoord_ranges(
        self.model.nmesh, self.model.mesh_facenum
    )

    mesh_facetexcoord = self.model.mesh_facetexcoord.flatten()
    mesh_facetexcoord = mesh_facetexcoord[
        mesh_facetexcoord_ranges[self.dataid] : mesh_facetexcoord_ranges[
            self.dataid + 1
        ]
    ]

    mesh_facetexcoord[mesh_facetexcoord == len(mesh_texcoord)] = 0
    return mesh_texcoord, mesh_facetexcoord

  def _get_mesh_geometry(self):
    mesh_vert_adr_from = self.model.mesh_vertadr[self.dataid]
    mesh_vert_adr_to = (
        self.model.mesh_vertadr[self.dataid + 1]
        if self.dataid < self.model.nmesh - 1
        else len(self.model.mesh_vert)
    )
    mesh_vert = self.model.mesh_vert[mesh_vert_adr_from:mesh_vert_adr_to]

    mesh_face_adr_from = self.model.mesh_faceadr[self.dataid]
    mesh_face_adr_to = (
        self.model.mesh_faceadr[self.dataid + 1]
        if self.dataid < self.model.nmesh - 1
        else len(self.model.mesh_face)
    )
    mesh_face = self.model.mesh_face[mesh_face_adr_from:mesh_face_adr_to]
    mesh_facenum = self.model.mesh_facenum[self.dataid]
    return mesh_vert, mesh_face, mesh_facenum

class USDPrimitiveMesh(USDObject):

  def __init__(
      self,
      mesh_config: dict,
      stage: Usd.Stage,
      geom: mujoco.MjvGeom,
      obj_name: str,
      rgba: np.ndarray = np.array([1, 1, 1, 1]),
      texture_file: Optional[str] = None,
  ):
    super().__init__(stage,
                     geom,
                     obj_name,
                     rgba,
                     texture_file)

    self.mesh_config = mesh_config
    self.prim_mesh = self.generate_primitive_mesh()

    mesh_path = f"{self.xform_path}/Mesh_{obj_name}"
    self.usd_mesh = UsdGeom.Mesh.Define(stage, mesh_path)
    self.usd_prim = stage.GetPrimAtPath(mesh_path)

    mesh_vert, mesh_face, mesh_facenum = self._get_mesh_geometry()
    self.usd_mesh.GetPointsAttr().Set(mesh_vert)
    self.usd_mesh.GetFaceVertexCountsAttr().Set(
        [3 for _ in range(mesh_facenum)]
    )
    self.usd_mesh.GetFaceVertexIndicesAttr().Set(mesh_face)

    # setting mesh uv properties
    mesh_texcoord, mesh_facetexcoord = self._get_uv_geometry()
    self.texcoords = UsdGeom.PrimvarsAPI(self.usd_mesh).CreatePrimvar(
        "UVMap", Sdf.ValueTypeNames.TexCoord2fArray, UsdGeom.Tokens.faceVarying
    )

    self.texcoords.Set(mesh_texcoord)
    self.texcoords.SetIndices(Vt.IntArray([i for i in range(mesh_facenum * 3)]))

    self._set_refinement_properties(self.usd_prim)

    if self.texture_file:
      self.attach_image_material(self.usd_mesh)
    else:
      self.attach_solid_material(self.usd_mesh)

  def generate_primitive_mesh(self):
    _, prim_mesh = shapes_component.mesh_generator(self.mesh_config)
    prim_mesh.translate(-prim_mesh.get_center())
    return prim_mesh

  def _get_uv_geometry(self):

    assert self.prim_mesh

    x_scale, y_scale = self.geom.texrepeat
    mesh_texcoord = np.array(self.prim_mesh.triangle_uvs)
    mesh_facetexcoord = np.asarray(self.prim_mesh.triangles)

    x_multiplier, y_multiplier = 1, 1
    if self.geom.texuniform:
      if "box" in self.mesh_config:
        x_multiplier, y_multiplier = self.mesh_config["box"]["width"], self.mesh_config["box"]["height"]
      elif "sphere" in self.mesh_config:
        x_multiplier, y_multiplier = self.mesh_config["sphere"]["radius"], self.mesh_config["sphere"]["radius"]
      
    mesh_texcoord[:, 0] *= x_scale * x_multiplier
    mesh_texcoord[:, 1] *= y_scale * y_multiplier

    return mesh_texcoord, mesh_facetexcoord.flatten()

  def _get_mesh_geometry(self):
    assert self.prim_mesh

    # get mesh geometry from the open3d mesh model
    mesh_vert = np.asarray(self.prim_mesh.vertices)
    mesh_face = np.asarray(self.prim_mesh.triangles)

    return mesh_vert, mesh_face, len(mesh_face)

class USDTendon(USDObject):
  
  def __init__(
      self,
      mesh_config: dict,
      stage: Usd.Stage,
      geom: mujoco.MjvGeom,
      obj_name: str,
      rgba: np.ndarray = np.array([1, 1, 1, 1]),
      texture_file: Optional[str] = None,
  ):
    super().__init__(stage,
                     geom,
                     obj_name,
                     rgba,
                     texture_file)

    self.mesh_config = mesh_config
    self.tendon_parts = self.generate_primitive_mesh()
    self.usd_refs = defaultdict(dict)

    for name, mesh in self.tendon_parts.items():
      part_xform_path = f"{self.xform_path}/Mesh_Xform_{name}"
      mesh_path = f"{part_xform_path}/Mesh_{obj_name}"
      self.usd_refs[name]["usd_xform"] = UsdGeom.Xform.Define(stage, part_xform_path)
      self.usd_refs[name]["usd_mesh"] = UsdGeom.Mesh.Define(stage, mesh_path)
      self.usd_refs[name]["usd_prim"] = stage.GetPrimAtPath(mesh_path)
      # adding ops for each of the part xforms
      self.usd_refs[name]["translate_op"] = self.usd_refs[name]["usd_xform"].AddTranslateOp()
      self.usd_refs[name]["scale_op"] = self.usd_refs[name]["usd_xform"].AddScaleOp()

    # setting mesh geometry properties for each of the parts in the tendon
    part_geometries = self._get_mesh_geometry()
    for name, part_geometry in part_geometries.items():
      self.usd_refs[name]["usd_mesh"].GetPointsAttr().Set(part_geometry["mesh_vert"])
      self.usd_refs[name]["usd_mesh"].GetFaceVertexCountsAttr().Set(
        [3 for _ in range(part_geometry["mesh_facenum"])]
      )
      self.usd_refs[name]["usd_mesh"].GetFaceVertexIndicesAttr().Set(part_geometry["mesh_face"])

    # setting uv properties for each of the parts in the tendon
    part_uv_geometries = self._get_uv_geometry()
    for name, part_uv_geometry in part_uv_geometries.items():
      self.texcoords = UsdGeom.PrimvarsAPI(self.usd_refs[name]["usd_mesh"]).CreatePrimvar(
          "UVMap", Sdf.ValueTypeNames.TexCoord2fArray, UsdGeom.Tokens.faceVarying
      )
      self.texcoords.Set(part_uv_geometry["mesh_texcoord"])
      self.texcoords.SetIndices(Vt.IntArray([i for i in range(part_geometry["mesh_facenum"] * 3)]))
    
    for name in self.usd_refs.keys(): 
      self._set_refinement_properties(self.usd_refs[name]["usd_prim"])
      if self.texture_file:
        self.attach_image_material(self.usd_refs[name]["usd_mesh"])
      else:
        self.attach_solid_material(self.usd_refs[name]["usd_mesh"])
    
  def generate_primitive_mesh(self):
    mesh_parts = {}
    for part_config in self.mesh_config:
      mesh_name, prim_mesh = shapes_component.mesh_generator(part_config)
      prim_mesh.translate(-prim_mesh.get_center())
      mesh_parts[mesh_name] = prim_mesh
    return mesh_parts
  
  def _get_uv_geometry(self):
    part_uv_geometries = defaultdict(dict)
    for name, mesh in self.tendon_parts.items():
      x_scale, y_scale = self.geom.texrepeat
      mesh_texcoord = np.array(mesh.triangle_uvs)
      mesh_facetexcoord = np.asarray(mesh.triangles)
      part_uv_geometries[name] = {
        "mesh_texcoord": mesh_texcoord,
        "mesh_facetexcoord": mesh_facetexcoord
      }
    return part_uv_geometries

  def _get_mesh_geometry(self):
    part_geometries = defaultdict(dict)
    for name, mesh in self.tendon_parts.items():
      # get mesh geometry from the open3d mesh model
      mesh_vert = np.asarray(mesh.vertices)
      mesh_face = np.asarray(mesh.triangles)
      part_geometries[name] = {
        "mesh_vert": mesh_vert,
        "mesh_face": mesh_face,
        "mesh_facenum": len(mesh_face)
      }
    return part_geometries

  def update(self, pos: np.ndarray, mat: np.ndarray, visible: bool, frame: int, scale: Optional[np.ndarray] = None):
    """Updates the position and orientation of an object in the scene for a given frame"""
    super().update(pos, mat, visible, frame, scale)
    for name in self.tendon_parts.keys():
      if "left" in name:
        translate = [0, 0, -scale[2] - (scale[0] / 2)]
        self.usd_refs[name]["translate_op"].Set(Gf.Vec3f(translate), frame)
      elif "right" in name:
        translate = [0, 0, scale[2] + (scale[0] / 2)]
        self.usd_refs[name]["translate_op"].Set(Gf.Vec3f(translate), frame)

  def update_scale(self, scale: np.ndarray, frame: int):
    """Updates the scale of the tendon"""
    for name in self.tendon_parts.keys():
      if "cylinder" in name:
        self.usd_refs[name]["scale_op"].Set(Gf.Vec3f(scale.tolist()), frame)
      else:
        hemisphere_scale = scale.tolist()
        hemisphere_scale[2] = hemisphere_scale[0]
        self.usd_refs[name]["scale_op"].Set(Gf.Vec3f(hemisphere_scale), frame)
    
    
