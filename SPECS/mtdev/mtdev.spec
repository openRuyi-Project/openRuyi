# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mtdev
Version:        1.1.7
Release:        %autorelease
Summary:        Multitouch Protocol Translation Library
License:        MIT
URL:            http://bitmath.org/code/mtdev
VCS:            git:http://bitmath.org/git/mtdev.git
#!RemoteAsset
Source0:        http://bitmath.org/code/mtdev/mtdev-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
The mtdev is a stand-alone library which transforms all variants of kernel MT
events to the slotted type B protocol. The events put into mtdev may be from
any MT device, specifically type A without contact tracking, type A with contact
tracking, or type B with contact tracking.

%package        devel
Summary:        Development files for the mtdev library
Requires:       pkgconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and a test utility for
developing applications that use the mtdev library.

%files
%doc README
%license COPYING
%{_libdir}/libmtdev.so.*

%files devel
%{_bindir}/mtdev-test
%{_includedir}/mtdev*.h
%{_libdir}/libmtdev.so
%{_libdir}/pkgconfig/mtdev.pc

%changelog
%autochangelog
