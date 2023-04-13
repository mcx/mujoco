# Copyright 2022 DeepMind Technologies Limited
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
"""Provides information about MuJoCo API enums.

DO NOT EDIT. THIS FILE IS AUTOMATICALLY GENERATED.
"""

from typing import Mapping

from .ast_nodes import EnumDecl

ENUMS: Mapping[str, EnumDecl] = dict([
    ('mjtDisableBit',
     EnumDecl(
         name='mjtDisableBit',
         declname='enum mjtDisableBit_',
         values=dict([
             ('mjDSBL_CONSTRAINT', 1),
             ('mjDSBL_EQUALITY', 2),
             ('mjDSBL_FRICTIONLOSS', 4),
             ('mjDSBL_LIMIT', 8),
             ('mjDSBL_CONTACT', 16),
             ('mjDSBL_PASSIVE', 32),
             ('mjDSBL_GRAVITY', 64),
             ('mjDSBL_CLAMPCTRL', 128),
             ('mjDSBL_WARMSTART', 256),
             ('mjDSBL_FILTERPARENT', 512),
             ('mjDSBL_ACTUATION', 1024),
             ('mjDSBL_REFSAFE', 2048),
             ('mjDSBL_SENSOR', 4096),
             ('mjDSBL_MIDPHASE', 8192),
             ('mjNDISABLE', 14),
         ]),
     )),
    ('mjtEnableBit',
     EnumDecl(
         name='mjtEnableBit',
         declname='enum mjtEnableBit_',
         values=dict([
             ('mjENBL_OVERRIDE', 1),
             ('mjENBL_ENERGY', 2),
             ('mjENBL_FWDINV', 4),
             ('mjENBL_SENSORNOISE', 8),
             ('mjENBL_MULTICCD', 16),
             ('mjNENABLE', 5),
         ]),
     )),
    ('mjtJoint',
     EnumDecl(
         name='mjtJoint',
         declname='enum mjtJoint_',
         values=dict([
             ('mjJNT_FREE', 0),
             ('mjJNT_BALL', 1),
             ('mjJNT_SLIDE', 2),
             ('mjJNT_HINGE', 3),
         ]),
     )),
    ('mjtGeom',
     EnumDecl(
         name='mjtGeom',
         declname='enum mjtGeom_',
         values=dict([
             ('mjGEOM_PLANE', 0),
             ('mjGEOM_HFIELD', 1),
             ('mjGEOM_SPHERE', 2),
             ('mjGEOM_CAPSULE', 3),
             ('mjGEOM_ELLIPSOID', 4),
             ('mjGEOM_CYLINDER', 5),
             ('mjGEOM_BOX', 6),
             ('mjGEOM_MESH', 7),
             ('mjNGEOMTYPES', 8),
             ('mjGEOM_ARROW', 100),
             ('mjGEOM_ARROW1', 101),
             ('mjGEOM_ARROW2', 102),
             ('mjGEOM_LINE', 103),
             ('mjGEOM_SKIN', 104),
             ('mjGEOM_LABEL', 105),
             ('mjGEOM_NONE', 1001),
         ]),
     )),
    ('mjtCamLight',
     EnumDecl(
         name='mjtCamLight',
         declname='enum mjtCamLight_',
         values=dict([
             ('mjCAMLIGHT_FIXED', 0),
             ('mjCAMLIGHT_TRACK', 1),
             ('mjCAMLIGHT_TRACKCOM', 2),
             ('mjCAMLIGHT_TARGETBODY', 3),
             ('mjCAMLIGHT_TARGETBODYCOM', 4),
         ]),
     )),
    ('mjtTexture',
     EnumDecl(
         name='mjtTexture',
         declname='enum mjtTexture_',
         values=dict([
             ('mjTEXTURE_2D', 0),
             ('mjTEXTURE_CUBE', 1),
             ('mjTEXTURE_SKYBOX', 2),
         ]),
     )),
    ('mjtIntegrator',
     EnumDecl(
         name='mjtIntegrator',
         declname='enum mjtIntegrator_',
         values=dict([
             ('mjINT_EULER', 0),
             ('mjINT_RK4', 1),
             ('mjINT_IMPLICIT', 2),
             ('mjINT_IMPLICITFAST', 3),
         ]),
     )),
    ('mjtCollision',
     EnumDecl(
         name='mjtCollision',
         declname='enum mjtCollision_',
         values=dict([
             ('mjCOL_ALL', 0),
             ('mjCOL_PAIR', 1),
             ('mjCOL_DYNAMIC', 2),
         ]),
     )),
    ('mjtCone',
     EnumDecl(
         name='mjtCone',
         declname='enum mjtCone_',
         values=dict([
             ('mjCONE_PYRAMIDAL', 0),
             ('mjCONE_ELLIPTIC', 1),
         ]),
     )),
    ('mjtJacobian',
     EnumDecl(
         name='mjtJacobian',
         declname='enum mjtJacobian_',
         values=dict([
             ('mjJAC_DENSE', 0),
             ('mjJAC_SPARSE', 1),
             ('mjJAC_AUTO', 2),
         ]),
     )),
    ('mjtSolver',
     EnumDecl(
         name='mjtSolver',
         declname='enum mjtSolver_',
         values=dict([
             ('mjSOL_PGS', 0),
             ('mjSOL_CG', 1),
             ('mjSOL_NEWTON', 2),
         ]),
     )),
    ('mjtEq',
     EnumDecl(
         name='mjtEq',
         declname='enum mjtEq_',
         values=dict([
             ('mjEQ_CONNECT', 0),
             ('mjEQ_WELD', 1),
             ('mjEQ_JOINT', 2),
             ('mjEQ_TENDON', 3),
             ('mjEQ_DISTANCE', 4),
         ]),
     )),
    ('mjtWrap',
     EnumDecl(
         name='mjtWrap',
         declname='enum mjtWrap_',
         values=dict([
             ('mjWRAP_NONE', 0),
             ('mjWRAP_JOINT', 1),
             ('mjWRAP_PULLEY', 2),
             ('mjWRAP_SITE', 3),
             ('mjWRAP_SPHERE', 4),
             ('mjWRAP_CYLINDER', 5),
         ]),
     )),
    ('mjtTrn',
     EnumDecl(
         name='mjtTrn',
         declname='enum mjtTrn_',
         values=dict([
             ('mjTRN_JOINT', 0),
             ('mjTRN_JOINTINPARENT', 1),
             ('mjTRN_SLIDERCRANK', 2),
             ('mjTRN_TENDON', 3),
             ('mjTRN_SITE', 4),
             ('mjTRN_BODY', 5),
             ('mjTRN_UNDEFINED', 1000),
         ]),
     )),
    ('mjtDyn',
     EnumDecl(
         name='mjtDyn',
         declname='enum mjtDyn_',
         values=dict([
             ('mjDYN_NONE', 0),
             ('mjDYN_INTEGRATOR', 1),
             ('mjDYN_FILTER', 2),
             ('mjDYN_MUSCLE', 3),
             ('mjDYN_USER', 4),
         ]),
     )),
    ('mjtGain',
     EnumDecl(
         name='mjtGain',
         declname='enum mjtGain_',
         values=dict([
             ('mjGAIN_FIXED', 0),
             ('mjGAIN_AFFINE', 1),
             ('mjGAIN_MUSCLE', 2),
             ('mjGAIN_USER', 3),
         ]),
     )),
    ('mjtBias',
     EnumDecl(
         name='mjtBias',
         declname='enum mjtBias_',
         values=dict([
             ('mjBIAS_NONE', 0),
             ('mjBIAS_AFFINE', 1),
             ('mjBIAS_MUSCLE', 2),
             ('mjBIAS_USER', 3),
         ]),
     )),
    ('mjtObj',
     EnumDecl(
         name='mjtObj',
         declname='enum mjtObj_',
         values=dict([
             ('mjOBJ_UNKNOWN', 0),
             ('mjOBJ_BODY', 1),
             ('mjOBJ_XBODY', 2),
             ('mjOBJ_JOINT', 3),
             ('mjOBJ_DOF', 4),
             ('mjOBJ_GEOM', 5),
             ('mjOBJ_SITE', 6),
             ('mjOBJ_CAMERA', 7),
             ('mjOBJ_LIGHT', 8),
             ('mjOBJ_MESH', 9),
             ('mjOBJ_SKIN', 10),
             ('mjOBJ_HFIELD', 11),
             ('mjOBJ_TEXTURE', 12),
             ('mjOBJ_MATERIAL', 13),
             ('mjOBJ_PAIR', 14),
             ('mjOBJ_EXCLUDE', 15),
             ('mjOBJ_EQUALITY', 16),
             ('mjOBJ_TENDON', 17),
             ('mjOBJ_ACTUATOR', 18),
             ('mjOBJ_SENSOR', 19),
             ('mjOBJ_NUMERIC', 20),
             ('mjOBJ_TEXT', 21),
             ('mjOBJ_TUPLE', 22),
             ('mjOBJ_KEY', 23),
             ('mjOBJ_PLUGIN', 24),
         ]),
     )),
    ('mjtConstraint',
     EnumDecl(
         name='mjtConstraint',
         declname='enum mjtConstraint_',
         values=dict([
             ('mjCNSTR_EQUALITY', 0),
             ('mjCNSTR_FRICTION_DOF', 1),
             ('mjCNSTR_FRICTION_TENDON', 2),
             ('mjCNSTR_LIMIT_JOINT', 3),
             ('mjCNSTR_LIMIT_TENDON', 4),
             ('mjCNSTR_CONTACT_FRICTIONLESS', 5),
             ('mjCNSTR_CONTACT_PYRAMIDAL', 6),
             ('mjCNSTR_CONTACT_ELLIPTIC', 7),
         ]),
     )),
    ('mjtConstraintState',
     EnumDecl(
         name='mjtConstraintState',
         declname='enum mjtConstraintState_',
         values=dict([
             ('mjCNSTRSTATE_SATISFIED', 0),
             ('mjCNSTRSTATE_QUADRATIC', 1),
             ('mjCNSTRSTATE_LINEARNEG', 2),
             ('mjCNSTRSTATE_LINEARPOS', 3),
             ('mjCNSTRSTATE_CONE', 4),
         ]),
     )),
    ('mjtSensor',
     EnumDecl(
         name='mjtSensor',
         declname='enum mjtSensor_',
         values=dict([
             ('mjSENS_TOUCH', 0),
             ('mjSENS_ACCELEROMETER', 1),
             ('mjSENS_VELOCIMETER', 2),
             ('mjSENS_GYRO', 3),
             ('mjSENS_FORCE', 4),
             ('mjSENS_TORQUE', 5),
             ('mjSENS_MAGNETOMETER', 6),
             ('mjSENS_RANGEFINDER', 7),
             ('mjSENS_JOINTPOS', 8),
             ('mjSENS_JOINTVEL', 9),
             ('mjSENS_TENDONPOS', 10),
             ('mjSENS_TENDONVEL', 11),
             ('mjSENS_ACTUATORPOS', 12),
             ('mjSENS_ACTUATORVEL', 13),
             ('mjSENS_ACTUATORFRC', 14),
             ('mjSENS_BALLQUAT', 15),
             ('mjSENS_BALLANGVEL', 16),
             ('mjSENS_JOINTLIMITPOS', 17),
             ('mjSENS_JOINTLIMITVEL', 18),
             ('mjSENS_JOINTLIMITFRC', 19),
             ('mjSENS_TENDONLIMITPOS', 20),
             ('mjSENS_TENDONLIMITVEL', 21),
             ('mjSENS_TENDONLIMITFRC', 22),
             ('mjSENS_FRAMEPOS', 23),
             ('mjSENS_FRAMEQUAT', 24),
             ('mjSENS_FRAMEXAXIS', 25),
             ('mjSENS_FRAMEYAXIS', 26),
             ('mjSENS_FRAMEZAXIS', 27),
             ('mjSENS_FRAMELINVEL', 28),
             ('mjSENS_FRAMEANGVEL', 29),
             ('mjSENS_FRAMELINACC', 30),
             ('mjSENS_FRAMEANGACC', 31),
             ('mjSENS_SUBTREECOM', 32),
             ('mjSENS_SUBTREELINVEL', 33),
             ('mjSENS_SUBTREEANGMOM', 34),
             ('mjSENS_CLOCK', 35),
             ('mjSENS_PLUGIN', 36),
             ('mjSENS_USER', 37),
         ]),
     )),
    ('mjtStage',
     EnumDecl(
         name='mjtStage',
         declname='enum mjtStage_',
         values=dict([
             ('mjSTAGE_NONE', 0),
             ('mjSTAGE_POS', 1),
             ('mjSTAGE_VEL', 2),
             ('mjSTAGE_ACC', 3),
         ]),
     )),
    ('mjtDataType',
     EnumDecl(
         name='mjtDataType',
         declname='enum mjtDataType_',
         values=dict([
             ('mjDATATYPE_REAL', 0),
             ('mjDATATYPE_POSITIVE', 1),
             ('mjDATATYPE_AXIS', 2),
             ('mjDATATYPE_QUATERNION', 3),
         ]),
     )),
    ('mjtLRMode',
     EnumDecl(
         name='mjtLRMode',
         declname='enum mjtLRMode_',
         values=dict([
             ('mjLRMODE_NONE', 0),
             ('mjLRMODE_MUSCLE', 1),
             ('mjLRMODE_MUSCLEUSER', 2),
             ('mjLRMODE_ALL', 3),
         ]),
     )),
    ('mjtWarning',
     EnumDecl(
         name='mjtWarning',
         declname='enum mjtWarning_',
         values=dict([
             ('mjWARN_INERTIA', 0),
             ('mjWARN_CONTACTFULL', 1),
             ('mjWARN_CNSTRFULL', 2),
             ('mjWARN_VGEOMFULL', 3),
             ('mjWARN_BADQPOS', 4),
             ('mjWARN_BADQVEL', 5),
             ('mjWARN_BADQACC', 6),
             ('mjWARN_BADCTRL', 7),
             ('mjNWARNING', 8),
         ]),
     )),
    ('mjtTimer',
     EnumDecl(
         name='mjtTimer',
         declname='enum mjtTimer_',
         values=dict([
             ('mjTIMER_STEP', 0),
             ('mjTIMER_FORWARD', 1),
             ('mjTIMER_INVERSE', 2),
             ('mjTIMER_POSITION', 3),
             ('mjTIMER_VELOCITY', 4),
             ('mjTIMER_ACTUATION', 5),
             ('mjTIMER_ACCELERATION', 6),
             ('mjTIMER_CONSTRAINT', 7),
             ('mjTIMER_POS_KINEMATICS', 8),
             ('mjTIMER_POS_INERTIA', 9),
             ('mjTIMER_POS_COLLISION', 10),
             ('mjTIMER_POS_MAKE', 11),
             ('mjTIMER_POS_PROJECT', 12),
             ('mjNTIMER', 13),
         ]),
     )),
    ('mjtCatBit',
     EnumDecl(
         name='mjtCatBit',
         declname='enum mjtCatBit_',
         values=dict([
             ('mjCAT_STATIC', 1),
             ('mjCAT_DYNAMIC', 2),
             ('mjCAT_DECOR', 4),
             ('mjCAT_ALL', 7),
         ]),
     )),
    ('mjtMouse',
     EnumDecl(
         name='mjtMouse',
         declname='enum mjtMouse_',
         values=dict([
             ('mjMOUSE_NONE', 0),
             ('mjMOUSE_ROTATE_V', 1),
             ('mjMOUSE_ROTATE_H', 2),
             ('mjMOUSE_MOVE_V', 3),
             ('mjMOUSE_MOVE_H', 4),
             ('mjMOUSE_ZOOM', 5),
             ('mjMOUSE_SELECT', 6),
         ]),
     )),
    ('mjtPertBit',
     EnumDecl(
         name='mjtPertBit',
         declname='enum mjtPertBit_',
         values=dict([
             ('mjPERT_TRANSLATE', 1),
             ('mjPERT_ROTATE', 2),
         ]),
     )),
    ('mjtCamera',
     EnumDecl(
         name='mjtCamera',
         declname='enum mjtCamera_',
         values=dict([
             ('mjCAMERA_FREE', 0),
             ('mjCAMERA_TRACKING', 1),
             ('mjCAMERA_FIXED', 2),
             ('mjCAMERA_USER', 3),
         ]),
     )),
    ('mjtLabel',
     EnumDecl(
         name='mjtLabel',
         declname='enum mjtLabel_',
         values=dict([
             ('mjLABEL_NONE', 0),
             ('mjLABEL_BODY', 1),
             ('mjLABEL_JOINT', 2),
             ('mjLABEL_GEOM', 3),
             ('mjLABEL_SITE', 4),
             ('mjLABEL_CAMERA', 5),
             ('mjLABEL_LIGHT', 6),
             ('mjLABEL_TENDON', 7),
             ('mjLABEL_ACTUATOR', 8),
             ('mjLABEL_CONSTRAINT', 9),
             ('mjLABEL_SKIN', 10),
             ('mjLABEL_SELECTION', 11),
             ('mjLABEL_SELPNT', 12),
             ('mjLABEL_CONTACTPOINT', 13),
             ('mjLABEL_CONTACTFORCE', 14),
             ('mjNLABEL', 15),
         ]),
     )),
    ('mjtFrame',
     EnumDecl(
         name='mjtFrame',
         declname='enum mjtFrame_',
         values=dict([
             ('mjFRAME_NONE', 0),
             ('mjFRAME_BODY', 1),
             ('mjFRAME_GEOM', 2),
             ('mjFRAME_SITE', 3),
             ('mjFRAME_CAMERA', 4),
             ('mjFRAME_LIGHT', 5),
             ('mjFRAME_CONTACT', 6),
             ('mjFRAME_WORLD', 7),
             ('mjNFRAME', 8),
         ]),
     )),
    ('mjtVisFlag',
     EnumDecl(
         name='mjtVisFlag',
         declname='enum mjtVisFlag_',
         values=dict([
             ('mjVIS_CONVEXHULL', 0),
             ('mjVIS_TEXTURE', 1),
             ('mjVIS_JOINT', 2),
             ('mjVIS_CAMERA', 3),
             ('mjVIS_ACTUATOR', 4),
             ('mjVIS_ACTIVATION', 5),
             ('mjVIS_LIGHT', 6),
             ('mjVIS_TENDON', 7),
             ('mjVIS_RANGEFINDER', 8),
             ('mjVIS_CONSTRAINT', 9),
             ('mjVIS_INERTIA', 10),
             ('mjVIS_SCLINERTIA', 11),
             ('mjVIS_PERTFORCE', 12),
             ('mjVIS_PERTOBJ', 13),
             ('mjVIS_CONTACTPOINT', 14),
             ('mjVIS_CONTACTFORCE', 15),
             ('mjVIS_CONTACTSPLIT', 16),
             ('mjVIS_TRANSPARENT', 17),
             ('mjVIS_AUTOCONNECT', 18),
             ('mjVIS_COM', 19),
             ('mjVIS_SELECT', 20),
             ('mjVIS_STATIC', 21),
             ('mjVIS_SKIN', 22),
             ('mjVIS_MIDPHASE', 23),
             ('mjNVISFLAG', 24),
         ]),
     )),
    ('mjtRndFlag',
     EnumDecl(
         name='mjtRndFlag',
         declname='enum mjtRndFlag_',
         values=dict([
             ('mjRND_SHADOW', 0),
             ('mjRND_WIREFRAME', 1),
             ('mjRND_REFLECTION', 2),
             ('mjRND_ADDITIVE', 3),
             ('mjRND_SKYBOX', 4),
             ('mjRND_FOG', 5),
             ('mjRND_HAZE', 6),
             ('mjRND_SEGMENT', 7),
             ('mjRND_IDCOLOR', 8),
             ('mjRND_CULL_FACE', 9),
             ('mjNRNDFLAG', 10),
         ]),
     )),
    ('mjtStereo',
     EnumDecl(
         name='mjtStereo',
         declname='enum mjtStereo_',
         values=dict([
             ('mjSTEREO_NONE', 0),
             ('mjSTEREO_QUADBUFFERED', 1),
             ('mjSTEREO_SIDEBYSIDE', 2),
         ]),
     )),
    ('mjtPluginCapabilityBit',
     EnumDecl(
         name='mjtPluginCapabilityBit',
         declname='enum mjtPluginCapabilityBit_',
         values=dict([
             ('mjPLUGIN_ACTUATOR', 1),
             ('mjPLUGIN_SENSOR', 2),
             ('mjPLUGIN_PASSIVE', 4),
         ]),
     )),
    ('mjtGridPos',
     EnumDecl(
         name='mjtGridPos',
         declname='enum mjtGridPos_',
         values=dict([
             ('mjGRID_TOPLEFT', 0),
             ('mjGRID_TOPRIGHT', 1),
             ('mjGRID_BOTTOMLEFT', 2),
             ('mjGRID_BOTTOMRIGHT', 3),
         ]),
     )),
    ('mjtFramebuffer',
     EnumDecl(
         name='mjtFramebuffer',
         declname='enum mjtFramebuffer_',
         values=dict([
             ('mjFB_WINDOW', 0),
             ('mjFB_OFFSCREEN', 1),
         ]),
     )),
    ('mjtFontScale',
     EnumDecl(
         name='mjtFontScale',
         declname='enum mjtFontScale_',
         values=dict([
             ('mjFONTSCALE_50', 50),
             ('mjFONTSCALE_100', 100),
             ('mjFONTSCALE_150', 150),
             ('mjFONTSCALE_200', 200),
             ('mjFONTSCALE_250', 250),
             ('mjFONTSCALE_300', 300),
         ]),
     )),
    ('mjtFont',
     EnumDecl(
         name='mjtFont',
         declname='enum mjtFont_',
         values=dict([
             ('mjFONT_NORMAL', 0),
             ('mjFONT_SHADOW', 1),
             ('mjFONT_BIG', 2),
         ]),
     )),
    ('mjtButton',
     EnumDecl(
         name='mjtButton',
         declname='enum mjtButton_',
         values=dict([
             ('mjBUTTON_NONE', 0),
             ('mjBUTTON_LEFT', 1),
             ('mjBUTTON_RIGHT', 2),
             ('mjBUTTON_MIDDLE', 3),
         ]),
     )),
    ('mjtEvent',
     EnumDecl(
         name='mjtEvent',
         declname='enum mjtEvent_',
         values=dict([
             ('mjEVENT_NONE', 0),
             ('mjEVENT_MOVE', 1),
             ('mjEVENT_PRESS', 2),
             ('mjEVENT_RELEASE', 3),
             ('mjEVENT_SCROLL', 4),
             ('mjEVENT_KEY', 5),
             ('mjEVENT_RESIZE', 6),
             ('mjEVENT_REDRAW', 7),
             ('mjEVENT_FILESDROP', 8),
         ]),
     )),
    ('mjtItem',
     EnumDecl(
         name='mjtItem',
         declname='enum mjtItem_',
         values=dict([
             ('mjITEM_END', -2),
             ('mjITEM_SECTION', -1),
             ('mjITEM_SEPARATOR', 0),
             ('mjITEM_STATIC', 1),
             ('mjITEM_BUTTON', 2),
             ('mjITEM_CHECKINT', 3),
             ('mjITEM_CHECKBYTE', 4),
             ('mjITEM_RADIO', 5),
             ('mjITEM_RADIOLINE', 6),
             ('mjITEM_SELECT', 7),
             ('mjITEM_SLIDERINT', 8),
             ('mjITEM_SLIDERNUM', 9),
             ('mjITEM_EDITINT', 10),
             ('mjITEM_EDITNUM', 11),
             ('mjITEM_EDITTXT', 12),
             ('mjNITEM', 13),
         ]),
     )),
])
