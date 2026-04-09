# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spirv-headers
Version:        1.4.335.0
Release:        %autorelease
Summary:        Header files from the SPIR-V registry
License:        MIT
URL:            https://github.com/KhronosGroup/SPIRV-Headers
#!RemoteAsset
Source0:        https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Header files from the SPIR-V registry.
This includes:
* Header files for various languages.
* JSON files describing the grammar.
* The XML registry file.

%package        devel
Summary:        Development files for %{name}

%description    devel
Development files for %{name}.

%prep -a
chmod a-x include/spirv/1.2/spirv.py

%files devel
%license LICENSE
%doc README.md
%{_includedir}/spirv/
%dir %{_datadir}/cmake/SPIRV-Headers/
%{_datadir}/cmake/SPIRV-Headers/*.cmake
%{_datadir}/pkgconfig/SPIRV-Headers.pc

%changelog
%autochangelog
