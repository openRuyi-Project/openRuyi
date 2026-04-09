# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global sover 15

Name:           log4cxx
Version:        1.6.1
Release:        %autorelease
Summary:        A port to C++ of the Log4j project
License:        Apache-2.0
URL:            https://logging.apache.org/log4cxx/index.html
VCS:            git:https://github.com/apache/logging-log4cxx.git
#!RemoteAsset:  sha256:187c85836f5b2f27fb1e8d77c7f1f2939725f1f6498b742b0dd569ba30965fd2
Source:         https://www.apache.org/dist/logging/log4cxx/%{version}/apache-log4cxx-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SITE:BOOL=OFF
# FIXME: Re-enable asyncappendertestcase after timeout/hang issue is resolved.
BuildOption(check):  -E "asyncappendertestcase"

BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  zip

%description
Log4cxx is a popular logging package written in C++. It features hierarchical
loggers, allowing for granular control over log output volume and cost.

%package        devel
Summary:        Development files for the Log4cxx C++ logging project
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config metadata, and CMake
configuration files needed to develop applications using Log4cxx.

%files
%license LICENSE
%doc NOTICE
%{_libdir}/liblog4cxx.so.%{sover}*

%files devel
%{_includedir}/log4cxx
%{_libdir}/liblog4cxx.so
%{_libdir}/pkgconfig/liblog4cxx.pc
%{_libdir}/cmake/log4cxx

%changelog
%autochangelog
