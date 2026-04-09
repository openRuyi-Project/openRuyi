# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glslang
Version:        1.4.335.0
Release:        %autorelease
Summary:        OpenGL and OpenGL ES shader front end and validator
License:        BSD-3-Clause AND GPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/KhronosGroup/glslang
#!RemoteAsset
Source0:        https://github.com/KhronosGroup/glslang/archive/refs/tags/vulkan-sdk-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DALLOW_EXTERNAL_SPIRV_TOOLS=ON
BuildOption(conf):  -DENABLE_OPT=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  python3

%description
glslang is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and libraries for glslang.

%files
%doc README.md
%{_bindir}/glslang
%{_bindir}/glslangValidator
%{_libdir}/*.so.*

%files devel
%{_includedir}/glslang/
%{_libdir}/*.so
%{_libdir}/cmake/glslang/

%changelog
%autochangelog
