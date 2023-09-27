cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

# create project
project(CeresHelloWorld)

# add dependencies
include(cmake/CPM.cmake)

CPMAddPackage("gh:fmtlib/fmt#7.1.3")
CPMAddPackage("gh:ceres-solver/ceres-solver#2.1.0")

# Ceres isn't set up to be built from source so packages it requires
# cannot be added with CPM and must be installed globally
find_package(Eigen3 3.3 REQUIRED)
find_package(glog 0.6.0 REQUIRED)

# add subdirectories
add_subdirectory(src)

# link dependencies
target_link_libraries(main fmt::fmt Ceres::ceres Eigen3::Eigen glog::glog)

# target_link_libraries(main fmt::fmt Eigen::Eigen)