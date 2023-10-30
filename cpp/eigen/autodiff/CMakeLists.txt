cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

# create project
project(eigen_autodiff_test)

find_package(Eigen3 3.3 REQUIRED)

set(CMAKE_CXX_STANDARD 20)
add_executable(main main.cpp)
target_link_libraries(main Eigen3::Eigen)