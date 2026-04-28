# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spirv-cross
Version:        1.4.335.0
Release:        %autorelease
Summary:        Tool and library for SPIR-V reflection and disassembly
License:        Apache-2.0 OR MIT
URL:            https://github.com/KhronosGroup/SPIRV-Cross
#!RemoteAsset:  sha256:c3e935cb19e2dda8e2e03fcfcbe451131595fec2cfbc73ab79a6f4c4cd43eb16
Source0:        https://github.com/KhronosGroup/SPIRV-Cross/archive/refs/tags/vulkan-sdk-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DSPIRV_CROSS_SHARED=ON
BuildOption(conf):  -DSPIRV_CROSS_CLI=ON

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
SPIRV-Cross is a tool and library designed for parsing and converting SPIR-V to
other shader languages. It can output GLSL, MSL or HLSL, and JSON reflection.

%package        devel
Summary:        Development headers for the SPIRV-Cross library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development headers and libraries for SPIRV-Cross.

%install -a
rm -fv %{buildroot}/%{_libdir}/*.a

for i in c core cpp glsl hlsl msl reflect util; do
	ln -s "libspirv-cross-c-shared.so" "%{buildroot}/%{_libdir}/libspirv-cross-$i.so"
done

%files
%license LICENSE
%doc README.md
%{_bindir}/spirv-cross
%{_libdir}/libspirv-cross-c-shared.so.*

%files devel
%{_libdir}/libspirv-cross-*.so
%{_libdir}/pkgconfig/spirv-cross-c-shared.pc
%{_libdir}/pkgconfig/spirv-cross-c.pc
%{_includedir}/spirv_cross/
%dir %_datadir/spirv*
%_datadir/spirv*/cmake/

%changelog
%autochangelog
