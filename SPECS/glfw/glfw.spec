# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glfw
Version:        3.4
Release:        %autorelease
Summary:        A cross-platform multimedia library
License:        Zlib
URL:            https://github.com/glfw/glfw
#!RemoteAsset:  sha256:c038d34200234d071fae9345bc455e4a8f2f544ab60150765d7704e08f3dac01
Source0:        https://github.com/glfw/glfw/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DGLFW_BUILD_EXAMPLES=OFF
BuildOption(conf):  -DGLFW_BUILD_TESTS=ON
BuildOption(conf):  -DGLFW_BUILD_DOCS=ON

BuildRequires:  cmake
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  doxygen
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(VulkanLoader)
BuildRequires:  pkgconfig(wayland-egl)

%description
GLFW is a free, Open Source, multi-platform library for OpenGL application
development that provides a powerful API for handling operating system specific
tasks such as opening an OpenGL window, reading keyboard, mouse, joystick and
time input, creating threads, and more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(dri)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xi)
Requires:       pkgconfig(xinerama)
Requires:       pkgconfig(xrandr)

%description    devel
The glfw-devel package contains header files for developing applications
using the GLFW library.

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libglfw.so.3*

%files devel
%{_includedir}/GLFW/
%{_libdir}/libglfw.so
%{_libdir}/pkgconfig/glfw3.pc
%{_libdir}/cmake/glfw3/
%doc %{_docdir}/GLFW/

%changelog
%autochangelog
