# Copyright 2021 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set(MUJOCO_TEST_INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/.. ${CMAKE_CURRENT_SOURCE_DIR}/../src)
set(MUJOCO_TEST_WORKING_DIR ${CMAKE_CURRENT_SOURCE_DIR})

include(GoogleTest)

# This macro is used to add a C++ test to MuJoCo CMake build system
#
# The CMake targets linked by default with target_link_libraries are:
#   mujoco fixture gmock
#
# The macro supports the following parameters:
#   * PROPERTIES: multiple value parameter, its value is set as test properties
#                 via the set_tests_properties(<test> PROPERTIES <argument>) function
#   * ADDITIONAL_LINK_LIBRARIES: multiple value parameter, additional libraries linked
#                                to the test via target_link_libraries
#   * MAIN_TARGET: single value parameter, used to specify the target linked to the tests
#                  that define the main entry poiny. If not indicated, gest_main is used
macro(mujoco_test name)
  set(options)
  set(oneValueArgs MAIN_TARGET)
  set(multiValueArgs PROPERTIES ADDITIONAL_LINK_LIBRARIES)
  cmake_parse_arguments(
    _ARGS
    "${options}"
    "${oneValueArgs}"
    "${multiValueArgs}"
    ${ARGN}
  )

  add_executable(${name} ${name}.cc)
  target_link_libraries(${name} mujoco fixture gmock)
  if(_ARGS_MAIN_TARGET)
    target_link_libraries(${name} ${_ARGS_MAIN_TARGET})
  else()
    target_link_libraries(${name} gtest_main)
  endif()
  if(_ARGS_ADDITIONAL_LINK_LIBRARIES)
    target_link_libraries(${name} ${_ARGS_ADDITIONAL_LINK_LIBRARIES})
  endif()
  target_include_directories(${name} PRIVATE ${MUJOCO_TEST_INCLUDE})
  set_target_properties(${name} PROPERTIES BUILD_RPATH ${CMAKE_LIBRARY_OUTPUT_DIRECTORY})
  # gtest_discover_tests is recommended over gtest_add_tests, but has some issues in Windows.
  gtest_add_tests(
    TARGET ${name}
    SOURCES ${name}.cc
    WORKING_DIRECTORY ${MUJOCO_TEST_WORKING_DIR}
    TEST_LIST testList
  )
  if(WIN32)
    set_tests_properties(
      ${testList} PROPERTIES ENVIRONMENT "PATH=$<TARGET_FILE_DIR:mujoco>;$ENV{PATH}"
    )
  endif()
  if(_ARGS_PROPERTIES)
    set_tests_properties(${testList} PROPERTIES ${_ARGS_PROPERTIES})
  endif()

endmacro()

add_library(fixture STATIC fixture.h fixture.cc)
target_include_directories(fixture PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/..)
target_compile_definitions(fixture PUBLIC MJSTATIC)

target_link_libraries(
  fixture
  PUBLIC absl::core_headers
         absl::synchronization
         absl::flat_hash_map
         absl::flat_hash_set
         gtest
         gmock
         mujoco::mujoco
)
target_include_directories(fixture PRIVATE ${mujoco_SOURCE_DIR}/include gmock)

mujoco_test(fixture_test)

mujoco_test(header_test)

mujoco_test(pipeline_test)

add_subdirectory(benchmark)
add_subdirectory(engine)
add_subdirectory(sample)
add_subdirectory(user)
add_subdirectory(xml)
add_subdirectory(plugin/elasticity)
add_subdirectory(plugin/actuator)
add_subdirectory(experimental)
