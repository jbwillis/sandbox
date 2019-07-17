
add_library(helloworld STATIC helloworld.c)
add_executable(main main.c)
target_link_libraries(main helloworld)
