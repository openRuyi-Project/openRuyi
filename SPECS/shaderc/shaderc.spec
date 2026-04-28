# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           shaderc
Version:        2026.1
Release:        %autorelease
Summary:        Collection of tools, libraries, and tests for Vulkan shader compilation
License:        Apache-2.0
URL:            https://github.com/google/shaderc
#!RemoteAsset:  sha256:245002feccbe7f8361b223545a5654cea69780745886872d7efff50a38d96c66
Source0:        https://github.com/google/shaderc/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

# use system lib to build,as same as opensuse.
Patch0:         0001-Use-system-third-party-libs.patch

BuildOption(conf):  -DCMAKE_SKIP_RPATH=True
BuildOption(conf):  -DPYTHON_EXECUTABLE=%{__python3}
BuildOption(conf):  -DSHADERC_SKIP_TESTS=True
BuildOption(conf):  -DCMAKE_CXX_FLAGS="-I/usr/include/glslang"

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(SPIRV-Headers)
BuildRequires:  cmake(glslang)

%description
A collection of tools, libraries and tests for shader compilation.

%package        devel
Summary:        Header files for the shaderc library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
A compiler library for GLSL/HLSL to SPIR-V.

%prep -a
chmod a+x utils/update_build_version.sh
echo "\"%version\"" >glslc/src/build-version.inc

%install -a
# Remove static libraries and their pkgconfig files
rm %buildroot/%_libdir/*.a
rm %buildroot/%_libdir/pkgconfig/shaderc_{static,combined}.pc

%files
%license LICENSE
%_bindir/glslc
%_libdir/libshaderc_shared.so.*

%files devel
%_includedir/shaderc/
%_libdir/libshaderc_shared.so
%_libdir/pkgconfig/shaderc.pc

%changelog
%autochangelog
