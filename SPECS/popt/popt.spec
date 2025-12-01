# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:    popt
Version: 1.19
Release: %autorelease
License: MIT
Summary: Command line option parsing library
URL:     https://github.com/rpm-software-management/popt
#!RemoteAsset
Source0: http://ftp.rpm.org/popt/releases/popt-1.x/popt-%{version}.tar.gz
Patch:   0001-popt-libc-updates.patch
BuildSystem:    autotools
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  automake
BuildRequires:  autoconf
BuildOption(conf): --disable-static

%description
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions. It
improves on them by allowing more powerful argument expansion. Popt can
parse arbitrary argv[] style arrays and automatically set variables
based on command line arguments.  Popt allows command line arguments to
be aliased via configuration files and includes utility functions for
parsing arbitrary strings into argv[] arrays using shell-like rules.


%package devel
Summary:        Development files for the popt library
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
The popt-devel package includes header files and libraries necessary
for developing programs which use the popt C library. It contains the
API documentation of the popt library, too.

%conf -p
autoreconf -fiv

%install -a
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%{_libdir}/libpopt.so.*

%files devel
%license COPYING
%doc README
%{_libdir}/libpopt.so
%{_includedir}/popt.h
%{_mandir}/man3/popt.3*
%{_libdir}/pkgconfig/popt.pc


%changelog
%{?autochangelog}
