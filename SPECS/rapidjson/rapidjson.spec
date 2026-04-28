# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define commit 24b5e7a

Name:           rapidjson
Version:        1.1.0.%{commit}
Release:        %autorelease
Summary:        Fast JSON parser and generator for C++
License:        MIT AND BSD-3-Clause
URL:            https://rapidjson.org/
VCS:            git:https://github.com/Tencent/rapidjson
#!RemoteAsset:  sha256:2d2601a82d2d3b7e143a3c8d43ef616671391034bc46891a9816b79cf2d3e7a8
Source:         https://github.com/Tencent/rapidjson/archive/%{commit}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DRAPIDJSON_BUILD_DOC:BOOL=ON
BuildOption(conf):  -DRAPIDJSON_BUILD_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DRAPIDJSON_BUILD_TESTS:BOOL=OFF
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  doxygen

%description
RapidJSON is a fast, self-contained, header-only C++ library for parsing
and generating JSON. It is compliant with RFC8259 and ECMA-404.

%package        devel
Summary:        Header files for the RapidJSON C++ library
Provides:       %{name}-static = %{version}-%{release}

%description    devel
This package contains the header files, CMake/pkg-config files, and
documentation needed to develop applications that use RapidJSON.

%prep -a
rm -rf thirdparty
find . -type f -name CMakeLists.txt -print0 | xargs -0 sed -i -e "s/-march=native/ /g" -e "s/-Werror//g"

%files devel
%license license.txt
%doc %{_docdir}/RapidJSON/
%{_libdir}/cmake/RapidJSON/
%{_libdir}/pkgconfig/RapidJSON.pc
%{_includedir}/rapidjson/

%changelog
%autochangelog
