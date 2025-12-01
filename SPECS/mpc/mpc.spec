# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mpc
Version:        1.3.1
Release:        %autorelease
Summary:        multiple-precision complex shared library
License:        LGPL-3.0-or-later
URL:            http://www.multiprecision.org/mpc/
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/mpc/mpc-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/mpc/mpc-%{version}.tar.gz.sig
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmp) >= 5.0.0
BuildRequires:  pkgconfig(mpfr) >= 4.1.0
BuildSystem:    autotools

%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package -n libmpc3
Summary:        MPC multiple-precision complex shared library

%description -n libmpc3
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package devel
Summary:        MPC multiple-precision complex library development files
Requires:       libmpc3 = %{version}
Requires:       pkgconfig(gmp) >= 5.0.0
Requires:       pkgconfig(mpfr) >= 4.1.0

%description devel
MPC multiple-precision complex library development files.

%check
%make_build check

%files -n libmpc3
%defattr(-,root,root)
%license COPYING.LESSER
%{_libdir}/libmpc.so.3*

%files devel
%defattr(-,root,root)
%license COPYING.LESSER
%doc AUTHORS NEWS
%{_infodir}/mpc.info*
%{_libdir}/libmpc.a
%{_libdir}/libmpc.so
%{_includedir}/mpc.h

%changelog
%{?autochangelog}
