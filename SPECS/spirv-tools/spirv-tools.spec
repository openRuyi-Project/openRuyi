# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spirv-tools
Version:        1.4.335.0
Release:        %autorelease
Summary:        API and commands for processing SPIR-V modules
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/SPIRV-Tools
#!RemoteAsset
Source0:        https://github.com/KhronosGroup/SPIRV-Tools/archive/refs/tags/vulkan-sdk-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DSPIRV-Headers_SOURCE_DIR=%{_prefix}
BuildOption(conf):  -DPYTHON_EXECUTABLE=%{__python3}
BuildOption(conf):  -DSPIRV_TOOLS_BUILD_STATIC=OFF
BuildOption(check):  -E spirv-tools-copyrights

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(SPIRV-Headers)

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(SPIRV-Headers)

%description    devel
Development files for %{name}.

%files
%license LICENSE
%doc README.md CHANGES
%{_bindir}/spirv-*
%{_libdir}/libSPIRV-Tools*.so

%files devel
%{_includedir}/spirv-tools/
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/SPIRV-Tools.pc
%{_libdir}/pkgconfig/SPIRV-Tools-shared.pc

%changelog
%autochangelog
