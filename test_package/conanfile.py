from conans import ConanFile, CMake


class DummyTestConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake_find_package"

    def build(self):
        self.cmake = CMake(self)
        print("{}".format(self.cmake.command_line))
        self.cmake.configure()
        self.cmake.build()

    def test(self):
        pass
