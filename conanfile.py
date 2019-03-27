from conans import ConanFile, CMake


class DummyConan(ConanFile):
    name = "dummy"
    version = "1.0"
    topics = ("cmake")
    # generators = "cmake_find_package"
    exports_sources = ["CMakeLists.txt", "*.cmake"]
    exports = ["*.cmake", "lib/cmake/*.cmake"]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.cmake")

    def package_info(self):
        self.cpp_info.builddirs = ["", "lib/cmake"] # root path and a subfolder

    def package_id(self):
        self.info.header_only()
