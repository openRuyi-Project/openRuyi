# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mpfr
Version:        4.2.2
Release:        %autorelease
Summary:        The GNU multiple-precision floating-point library
License:        LGPL-3.0-or-later
URL:            https://www.mpfr.org/
VCS:            git:https://gitlab.inria.fr/mpfr/mpfr.git
#!RemoteAsset
Source0:        https://www.mpfr.org/mpfr-%{version}/mpfr-%{version}.tar.xz
#!RemoteAsset
Source1:        https://www.mpfr.org/mpfr-%{version}/mpfr-%{version}.tar.xz.asc
Buildsystem:    autotools

BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig

%description
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit
mantissa).

%package        devel
Summary:        Development files for the GNU multiple-precision floating-point library
Requires:       pkgconfig(gmp)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for the GNU multiple-precision floating-point library.

The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

%conf
%configure \
      --enable-thread-safe \
      --enable-shared \
      --disable-static \
      --docdir=%{_docdir}/%{name}

%files
%license COPYING*
%{_libdir}/libmpfr.so.6*

%files devel
%license COPYING*
%doc %{_docdir}/mpfr
%{_infodir}/mpfr.info*
%{_libdir}/libmpfr.so
%{_includedir}/mpf2mpfr.h
%{_includedir}/mpfr.h
%{_libdir}/pkgconfig/mpfr.pc

%changelog
%autochangelog
