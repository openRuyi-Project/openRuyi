# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cfortran
Version:        20210827
Release:        %autorelease
Summary:        Header for interfacing C or C++ with Fortran
License:        LGPL-2.0-or-later
URL:            https://github.com/bastien-roucaries/cfortran
#!RemoteAsset:  sha256:d1e3ce2c1d85fa4854d6a9276df333962a662426c618c4f011a9546bae55afda
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

# https://github.com/bastien-roucaries/cfortran/pull/3
Patch2000:      2000-Fix-fstr_test-coredump-with-D_FORTIFY_SOURCE-3-and-O.patch

# need add -std=gnu17: https://github.com/bastien-roucaries/cfortran/issues/2
BuildOption(build):  CFLAGS="%{optflags} -std=gnu17"
BuildOption(check):  CFLAGS="%{optflags} -std=gnu17"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-fortran
BuildRequires:  libtool
BuildRequires:  make

%description
cfortran.h provides portable preprocessor macros for interfacing C or C++
code with Fortran routines.

%conf -p
autoreconf -fiv

%check -a
make distclean
rmdir eg/*/.deps

%files
%doc NEWS README.html eg
%license COPYING
%{_includedir}/cfortran.h

%changelog
%autochangelog
