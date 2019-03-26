cmake_minimum_required(VERSION 3.5)

project(dummy
	LANGUAGES NONE
	VERSION 1.0
)

include(GNUInstallDirs)

install(FILES dummy-config.cmake my-super-cmake-file.cmake
	DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)
