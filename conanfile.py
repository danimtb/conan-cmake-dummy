from conans import ConanFile, CMake


class DummyConan(ConanFile):
    name = "dummy"
    version = "1.0"
    topics = ("cmake")
    generators = "cmake_find_package"
    exports_sources = ["CMakeLists.txt", "dummy-config.cmake", "my-super-cmake-file.cmake"]

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()

        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()


