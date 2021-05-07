
add_library(helloworld STATIC helloworld.c)
add_executable(main.out main.c)
target_link_libraries(main.out helloworld)
