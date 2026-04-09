# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dejagnu
Version:        1.6.3
Release:        %autorelease
Summary:        Framework for Running Test Suites on Software Tools
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/dejagnu/
VCS:            git:https://https.git.savannah.gnu.org/git/dejagnu.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
#!RemoteAsset
Source2:        https://savannah.gnu.org/project/release-gpgkeys.php?group=dejagnu&download=1#/%{name}.keyring
Source3:        site.exp
BuildArch:      noarch
Buildsystem:    autotools

Patch0:         testsuite-legacy.patch

BuildOption(build):  -C build
BuildOption(install):  -C build DESTDIR=%{buildroot}
BuildOption(check):  -C build

BuildRequires:  expect
BuildRequires:  fdupes
BuildRequires:  gcc-c++

Requires:       expect
Requires:       texinfo
Requires:       tcl

%description
DejaGnu is a framework for testing other programs.  Its purpose is to
provide a single front-end for all tests.  Beyond this, DejaGnu offers
several advantages for testing:

1. The flexibility and consistency of the DejaGnu framework make it
   easy to write tests for any program.

1. DejaGnu provides a layer of abstraction that allows you to write
   tests that are portable to any host or target where a program
   must be tested.  For instance, a test for GDB can run (from any
   Unix-based host) on any target architecture that DejaGnu
   supports.

1. All tests have the same output format.  This makes it easy to
   integrate testing into other software development processes.
   DejaGnu's output is designed to be parsed by other filtering
   scripts and it is also human-readable.

DejaGnu is written in expect, which in turn uses "Tcl"--Tool command
language.

Running tests requires two things: the testing framework and the test
suites themselves.

%conf
mkdir build
cd build
# 49078@debbugs.gnu.org: bug in Expect 5.45.4 triggers a testsuite failure
# when building in source directory
%define _configure ../configure
%configure

%install -a
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/dejagnu/site.exp
ln -s -f %{_sysconfdir}/dejagnu/site.exp %{buildroot}%{_datadir}/dejagnu/site.exp

%files
%defattr(-, root, root)
%license COPYING
%doc ChangeLog NEWS README AUTHORS TODO
%dir %{_datadir}/dejagnu
%dir %{_sysconfdir}/dejagnu
%{_bindir}/dejagnu
%{_bindir}/runtest
%{_mandir}/man1/dejagnu.1%{ext_man}
%{_mandir}/man1/dejagnu-help.1%{ext_man}
%{_mandir}/man1/dejagnu-report-card.1%{ext_man}
%{_mandir}/man1/runtest.1%{ext_man}
%{_infodir}/dejagnu.info%{ext_info}
%{_includedir}/*
%config(noreplace) %{_sysconfdir}/dejagnu/site.exp
%{_datadir}/dejagnu/*

%changelog
%autochangelog
