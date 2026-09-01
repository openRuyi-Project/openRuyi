# This file is called macros.aaa-buildsystem.cmake
# to sort alphabetically before macros.buildsystem.cmake.
# When this file is installed but macros.buildsystem.cmake is not
# this macro will cause the package with the real macro to be installed.
# When macros.buildsystem.cmake is installed, it overrides this macro.
# Note: This takes arbitrary options, to ease addition of new options to the real macro.
%cmake_buildrequires(-) echo 'cmake' && exit 0

# Declarative buildsystem, requires RPM 4.20+ to work
# https://rpm-software-management.github.io/rpm/manual/buildsystem.html
%buildsystem_cmake_conf() %nil
%buildsystem_cmake_generate_buildrequires() %cmake_buildrequires %*
%buildsystem_cmake_build() %nil
%buildsystem_cmake_install() %nil
%buildsystem_cmake_check() %nil
