# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gmp
Version:        6.3.0
Release:        %autorelease
Summary:        A GNU multiple precision arithmetic library
URL:            https://gmplib.org
VCS:            hg:https://gmplib.org/repo/gmp
#!RemoteAsset
Source0:        https://gmplib.org/download/gmp/gmp-%{version}.tar.xz
License:        (LGPL-3.0-or-later OR GPL-2.0-or-later OR (LGPL-3.0-or-later AND GPL-2.0-or-later)) AND GFDL-1.3-invariants-or-later
BuildSystem:    autotools

BuildOption(conf):  --enable-cxx

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  m4

%description
GMP is a portable library written in C for arbitrary precision arithmetic
on integers, rational numbers, and floating-point numbers. It aims to provide
the fastest possible arithmetic for all applications that need higher
precision than is directly supported by the basic C types.

%package        devel
Summary:        Development library package for GMP.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Devel package include header files, documentation and libraries for GMP

%conf -p
export CFLAGS="$CFLAGS -std=gnu17"

%install -a
install -m 644 gmp-mparam.h ${RPM_BUILD_ROOT}%{_includedir}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%check -p
export LD_LIBRARY_PATH=`pwd`/.libs

%files
%license COPYING COPYING.LESSERv3 COPYINGv2 COPYINGv3
%doc NEWS README
%{_libdir}/libgmp.so.*
# libgmpxx
%{_libdir}/libgmpxx.so.*

%files devel
%{_libdir}/libgmpxx.so
%{_libdir}/libgmp.so
%{_includedir}/*.h
%{_infodir}/gmp.info*
%{_libdir}/libgmpxx.a
%{_libdir}/libgmp.a
%{_libdir}/pkgconfig/gmp.pc
%{_libdir}/pkgconfig/gmpxx.pc

%changelog
%autochangelog
