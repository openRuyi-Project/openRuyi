# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           log4cxx
Version:        1.5.0
Release:        %autorelease
Summary:        A port to C++ of the Log4j project
License:        Apache-2.0
URL:            https://logging.apache.org/log4cxx/index.html
#!RemoteAsset
Source:         https://www.apache.org/dist/logging/log4cxx/%{version}/apache-log4cxx-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DBUILD_SITE:BOOL=OFF

BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: openldap-devel
BuildRequires: zip

%description
Log4cxx is a popular logging package written in C++. It features hierarchical
loggers, allowing for granular control over log output volume and cost.

%package        devel
Summary:        Development files for the Log4cxx C++ logging project
Requires:       %{name} = %{version}

%description    devel
This package contains the header files, documentation, and other files needed
to develop applications using the Log4cxx library.

%files
%license LICENSE
%doc NOTICE KEYS
%{_libdir}/liblog4cxx.so.15*

%files devel
%{_includedir}/log4cxx
%{_libdir}/liblog4cxx.so
%{_libdir}/pkgconfig/liblog4cxx.pc
%{_libdir}/cmake/log4cxx

%changelog
%{?autochangelog}
