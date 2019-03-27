from conans import ConanFile, CMake


class DummyTestConan(ConanFile):
    settings = "os"
    generators = "cmake_find_package"
    requires = "dummy/1.0@demo/testing"

    def build_requirements(self):
        self.build_requires("dummy/1.0@demo/testing")

    def build(self):
        self.cmake = CMake(self)

        print("{}".format(self.cmake.command_line))

        self.cmake.configure()
        self.cmake.build()


    def test(self):
        self.cmake.test()

