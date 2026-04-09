# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define VER 2_1_2

Name:           log4cplus
Version:        2.1.2
Release:        %autorelease
Summary:        C++ logging library
License:        Apache-2.0
URL:            https://github.com/log4cplus/log4cplus
#!RemoteAsset
Source0:        https://github.com/log4cplus/log4cplus/releases/download/REL_%{VER}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://github.com/log4cplus/log4cplus/releases/download/REL_%{VER}/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc-c++
BuildRequires:  make

%description
log4cplus is a simple to use C++ logging API providing thread--safe,
flexible, and arbitrarily granular control over log management and
configuration. It is modeled after the Java log4j API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides headers and libraries needed to develop applications
using log4cplus.

%files
%license LICENSE
%doc README.md ChangeLog
%_libdir/lib*.so*

%files devel
%{_includedir}/log4cplus
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/log4cplus.pc

%changelog
%autochangelog
