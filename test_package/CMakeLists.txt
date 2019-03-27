cmake_minimum_required(VERSION 3.5)

project(test_dummy
	LANGUAGES NONE
)

message("CMAKE_MODULE_PATH: ${CMAKE_MODULE_PATH}")

find_package(dummy REQUIRED)
message("dummy_MODULE_PATH: ${dummy_MODULE_PATH}")
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${dummy_MODULE_PATH})

include(my-super-cmake-file)

do_some_incredible_stuff()
