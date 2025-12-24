# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name   CUnit
%define _version 2.1-3
Name:           cunit
Version:        2.1.3
Release:        %autorelease
Summary:        A basic unit testing framework for C
License:        LGPL-2.0-only
URL:            https://cunit.sourceforge.net/
#!RemoteAsset
Source:         https://download.sourceforge.net/cunit/%{_name}-%{_version}.tar.bz2
Patch1:         0001-cunit-link-ncurses.patch
Patch2:         0002-cunit-ncurses6.patch
BuildSystem:    autotools

BuildOption(conf):    --disable-static
BuildOption(conf):    --enable-automated
BuildOption(conf):    --enable-basic
BuildOption(conf):    --enable-console
BuildOption(conf):    --enable-curses

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  perl

%description
CUnit is a unit testing framework for C.
This package installs the CUnit static library,
headers, and documentation files.

%package        devel
Summary:        CUnit development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ncurses-devel
Requires:       pkgconfig

%description    devel
CUnit is a unit testing framework for C.
This package installs the CUnit development files.

%package        doc
Summary:        CUnit documentation

%description    doc
CUnit is a unit testing framework for C.
This package installs the CUnit documentation files.

%conf -p
autoreconf -fi

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/libcunit.so.1
%{_libdir}/libcunit.so.1.*

%files devel
%dir %{_includedir}/CUnit
%{_includedir}/CUnit/*
%{_libdir}/libcunit.so
%{_libdir}/pkgconfig/cunit.pc

%files doc
%doc /usr/doc/CUnit
%{_datadir}/CUnit/*
%{_mandir}/man3/CUnit.3*

%changelog
%{?autochangelog}
