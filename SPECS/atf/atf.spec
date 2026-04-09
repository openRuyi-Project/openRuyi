# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           atf
Version:        0.23
Release:        %autorelease
Summary:        Automated Testing Framework (metapackage)
License:        BSD-2-Clause
URL:            https://github.com/freebsd/atf
#!RemoteAsset
Source:         https://github.com/freebsd/atf/archive/refs/tags/atf-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  INSTALL="install -p"
BuildOption(conf):  --disable-static
BuildOption(build):   pkgtestsdir=%{_libexecdir}/atf/tests
BuildOption(build):   testsdir=%{_libexecdir}/atf/tests
BuildOption(install):  pkgtestsdir=%{_libexecdir}/atf/tests
BuildOption(install):  testsdir=%{_libexecdir}/atf/tests

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
The Automated Testing Framework (ATF) is a collection of libraries
to implement test programs in a variety of languages.

%conf -p
autoreconf -is

%files
%dir %{_datadir}/atf
%doc %{_docdir}/atf
%{_bindir}/atf-sh
%{_datadir}/aclocal/atf-c++.m4
%{_datadir}/aclocal/atf-c.m4
%{_datadir}/aclocal/atf-common.m4
%{_datadir}/aclocal/atf-sh.m4
%{_datadir}/atf/
%{_includedir}/atf-c++.hpp
%{_includedir}/atf-c++/
%{_includedir}/atf-c.h
%{_includedir}/atf-c/
%{_libdir}/libatf-c++.so
%{_libdir}/libatf-c++.so.2*
%{_libdir}/libatf-c.so
%{_libdir}/libatf-c.so.1*
%{_libdir}/pkgconfig/atf-c++.pc
%{_libdir}/pkgconfig/atf-c.pc
%{_libdir}/pkgconfig/atf-sh.pc
%{_libexecdir}/atf-check
%{_libexecdir}/atf/tests
%{_mandir}/man1/atf-check.1*
%{_mandir}/man1/atf-sh.1*
%{_mandir}/man1/atf-test-program.1*
%{_mandir}/man3/atf-c++.3*
%{_mandir}/man3/atf-c.3*
%{_mandir}/man3/atf-sh.3*
%{_mandir}/man4/atf-test-case.4*
%{_mandir}/man7/atf.7*

%changelog
%autochangelog
