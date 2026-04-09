# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           check
Version:        0.15.2
Release:        %autorelease
Summary:        A unit testing framework for C
License:        LGPL-2.1-or-later
URL:            https://libcheck.github.io/check/
VCS:            git:https://github.com/libcheck/check
#!RemoteAsset
Source:         https://github.com/libcheck/check/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-option-checking MAKEINFO=true

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  texinfo

%description
Check is a unit testing framework for C. It features a simple interface for
defining unit tests, putting them into a test suite, and running them.
Tests can be run in a separate address space, so Check can catch segment faults.

%package        devel
Summary:        Development files for the Check unit testing framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and pkg-config file
needed to develop applications and tests that use the Check framework.

%conf -p
autoreconf -fi

%files
%license COPYING.LESSER
%{_libdir}/libcheck.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README.md THANKS TODO
%doc %{_docdir}/check
%{_bindir}/checkmk
%{_includedir}/*.h
%{_libdir}/libcheck.so
%{_libdir}/libcheck.a
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4
%{_mandir}/man1/checkmk.1*

%changelog
%autochangelog
