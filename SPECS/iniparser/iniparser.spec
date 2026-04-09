# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iniparser
Version:        4.2.6
Release:        %autorelease
Summary:        C library for parsing "INI-style" files
License:        MIT
URL:            https://gitlab.com/iniparser/iniparser
#!RemoteAsset
Source0:        https://gitlab.com/iniparser/iniparser/-/archive/v%{version}/iniparser-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTS=ON
BuildOption(conf):  -DBUILD_EXAMPLES=ON
BuildOption(conf):  -DBUILD_DOCS=OFF
BuildOption(conf):  -DBUILD_STATIC_LIBS=OFF

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
iniParser is an ANSI C library to parse "INI-style" files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for iniparser.

%files
%doc AUTHORS FAQ-en.md README.md
%license LICENSE
%{_libdir}/libiniparser.so.*
%{_docdir}/iniparser/examples

%files devel
%{_libdir}/libiniparser.so
%{_includedir}/iniparser/
%{_libdir}/cmake/iniparser/
%{_libdir}/pkgconfig/iniparser.pc

%changelog
%autochangelog
