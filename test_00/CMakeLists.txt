cmake_minimum_required(VERSION 3.15...3.31)

project(
  raspberry-pi-test_00
  VERSION 0.0
  LANGUAGES CXX)

add_executable(test_00 ${PROJECT_SOURCE_DIR}/src/main.cc)

# Link to wiringPi
target_link_libraries(test_00 wiringPi)

add_custom_target(clean-all
   COMMAND ${CMAKE_BUILD_TOOL} clean
   COMMAND ${CMAKE_COMMAND} -P clean-all.cmake
)