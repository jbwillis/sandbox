cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

# create project
project(eigen_variable_type_input)

set(CMAKE_CXX_STANDARD 20)

find_package(Eigen3 3.3 REQUIRED)

# link dependencies
add_library(eigenstuff eigenstuff.cpp)
target_link_libraries(eigenstuff Eigen3::Eigen)

add_executable(main main.cpp)
target_link_libraries(main Eigen3::Eigen eigenstuff)