# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nlohmann-json
Version:        3.12.0
Release:        %autorelease
Summary:        JSON for Modern C++ (header-only)
License:        MIT
URL:            https://github.com/nlohmann/json
#!RemoteAsset
Source:         https://github.com/nlohmann/json/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DJSON_MultipleHeaders:BOOL=ON
BuildOption(conf):  -DJSON_BuildTests:BOOL=OFF
BuildOption(conf):  -DJSON_Install:BOOL=ON

BuildRequires:  doctest
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
JSON for Modern C++ is a header-only C++ library for reading, writing,
and manipulating JSON data.

%files
%license LICENSE.MIT
%doc README.md
%{_includedir}/nlohmann
%{_datadir}/cmake/nlohmann_json/*.cmake
%{_datadir}/pkgconfig/nlohmann_json.pc

%changelog
%autochangelog
