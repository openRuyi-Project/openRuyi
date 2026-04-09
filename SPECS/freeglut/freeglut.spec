# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           freeglut
Version:        3.8.0
Release:        %autorelease
Summary:        A freely licensed alternative to the GLUT library
License:        MIT
URL:            https://github.com/freeglut/freeglut
#!RemoteAsset
Source0:        https://github.com/freeglut/freeglut/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFREEGLUT_BUILD_STATIC_LIBS=OFF

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(gl)

%description
freeglut is a completely open source alternative to the OpenGL Utility Toolkit
(GLUT) library. It allows the user to create and manage windows containing
OpenGL contexts.

%package        devel
Summary:        Freeglut developmental libraries and header files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)

%description    devel
Developmental libraries and header files required for developing or compiling
software which links to the freeglut library.

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_libdir}/libglut.so.3*

%files devel
%{_includedir}/GL/*.h
%{_libdir}/libglut.so
%{_libdir}/pkgconfig/glut.pc
%{_libdir}/cmake/FreeGLUT/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
