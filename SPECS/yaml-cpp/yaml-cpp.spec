# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           yaml-cpp
Version:        0.8.0
Release:        %autorelease
Summary:        A YAML parser and emitter for C++
License:        MIT
URL:            https://github.com/jbeder/yaml-cpp
#!RemoteAsset
Source0:        https://github.com/jbeder/yaml-cpp/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

Patch0:         0001-fix-include.patch

BuildOption(conf):  -DCMAKE_BUILD_TYPE=RelWithDebInfo
BuildOption(conf):  -DYAML_CPP_BUILD_TOOLS:BOOL=OFF
BuildOption(conf):  -DYAML_CPP_FORMAT_SOURCE:BOOL=OFF
BuildOption(conf):  -DYAML_CPP_INSTALL:BOOL=ON
BuildOption(conf):  -DYAML_BUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc CONTRIBUTING.md README.md
%license LICENSE
%{_libdir}/libyaml-cpp.so.*

%files devel
%{_includedir}/yaml-cpp/
%{_libdir}/libyaml-cpp.so
%{_libdir}/cmake/yaml-cpp/
%{_libdir}/pkgconfig/yaml-cpp.pc

%changelog
%autochangelog
