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
#!RemoteAsset:  sha256:37aa5341f2b51ffee245db3456d9bc25f718ca12beb7b990dc16d686890115e3
Source:         https://github.com/freebsd/atf/archive/refs/tags/atf-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  INSTALL="install -p"
BuildOption(conf):  --disable-static
BuildOption(build):  pkgtestsdir=%{_libexecdir}/atf/tests
BuildOption(build):  testsdir=%{_libexecdir}/atf/tests
BuildOption(install):  pkgtestsdir=%{_libexecdir}/atf/tests
BuildOption(install):  testsdir=%{_libexecdir}/atf/tests

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
The Automated Testing Framework (ATF) is a collection of libraries
to implement test programs in a variety of languages.

%package        tests
Summary:        Installed self-tests for ATF
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       kyua
Requires:       gcc
Requires:       gcc-c++

%description    tests
Self-test programs, Kyuafile manifests and source snippets for the ATF
C, C++ and shell interfaces. The tests use Kyua; compilation checks also
require the C and C++ compilers.

%conf -p
autoreconf -is

%files
%exclude %{_libexecdir}/atf/tests/
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

%files tests
%{_libexecdir}/atf/tests/

%changelog
%autochangelog
