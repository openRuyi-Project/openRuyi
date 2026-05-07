# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mpc
Version:        1.4.1
Release:        %autorelease
Summary:        multiple-precision complex shared library
License:        LGPL-3.0-or-later
URL:            http://www.multiprecision.org/mpc/
VCS:            git:https://gitlab.inria.fr/mpc/mpc
#!RemoteAsset:  sha256:91204cd32f164bd3b7c992d4a6a8ce6519511aadab30f78b6982d0bf8d73e931
Source0:        https://ftpmirror.gnu.org/gnu/mpc/mpc-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)

%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package        devel
Summary:        MPC multiple-precision complex library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gmp)
Requires:       pkgconfig(mpfr)

%description    devel
MPC multiple-precision complex library development files.

%check
%make_build check

%files
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
%{_libdir}/pkgconfig/mpc.pc
%{_includedir}/mpc.h

%changelog
%autochangelog
