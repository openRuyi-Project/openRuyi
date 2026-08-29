# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libiberty
Version:        16.1.0
Release:        %autorelease
Summary:        GNU libiberty static library
License:        GPL-3.0-or-later
URL:            https://gcc.gnu.org/
VCS:            git:https://gcc.gnu.org/git/gcc.git
#!RemoteAsset:  sha256:50efb4d94c3397aff3b0d61a5abd748b4dd31d9d3f2ab7be05b171d36a510f79
Source0:        https://ftpmirror.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(build):  -C libiberty
BuildOption(install):  -C libiberty
BuildOption(check):  -C libiberty

BuildRequires:  gcc
BuildRequires:  make

%description
libiberty is a collection of utility functions used by GNU tools such as GCC,
GDB, and binutils. This package builds only the standalone libiberty static
library from the GCC source tree.

%package        devel
Summary:        Development files for GNU libiberty

%description    devel
This package contains the static libiberty library and development headers.

%conf
cd libiberty
./configure --prefix=%{_prefix} --libdir=%{_libdir} --includedir=%{_includedir} --build=%{_build} --host=%{_host} --enable-install-libiberty

%files devel
%doc libiberty/README
%license COPYING COPYING.LIB COPYING3 COPYING3.LIB COPYING.RUNTIME
%{_libdir}/libiberty.a
%{_includedir}/libiberty/*.h

%changelog
%autochangelog
