# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libconfig
Version:        1.8.1
Release:        %autorelease
Summary:        C/C++ configuration file library
License:        LGPL-2.1-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
URL:            https://hyperrealm.github.io/libconfig/
VCS:            git:https://github.com/hyperrealm/libconfig
#!RemoteAsset
Source:         https://github.com/hyperrealm/libconfig/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTS:BOOL=OFF
BuildOption(conf):  -DBUILD_EXAMPLES:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  make

%description
Libconfig is a simple library for manipulating structured configuration files.
This format is more compact and more readable than XML, and unlike XML, it is
type-aware, so it is not necessary to do string parsing in application code.

%package        devel
Summary:        Development files for libconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development libraries and headers for developing software against libconfig.

%files
%license COPYING.LIB
%doc AUTHORS ChangeLog README
%{_libdir}/libconfig*.so.*

%files devel
%{_includedir}/libconfig*
%{_libdir}/cmake/libconfig
%{_libdir}/libconfig*.so
%{_libdir}/pkgconfig/libconfig++.pc
%{_libdir}/pkgconfig/libconfig.pc

%changelog
%{?autochangelog}
