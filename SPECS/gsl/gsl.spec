# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gsl
Version:        2.8
Release:        %autorelease
Summary:        The GNU Scientific Library for numerical analysis
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gsl/
VCS:            git:https://git.savannah.gnu.org/git/gsl.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/gsl/gsl-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --disable-static
BuildOption(conf):  CFLAGS="%{optflags} -ffp-contract=off"

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  make

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package        devel
Summary:        Libraries and the header files for GSL development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The gsl-devel package contains the header files necessary for
developing programs using the GSL (GNU Scientific Library).

%install -a
rm -rf %{buildroot}%{_infodir}/dir

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/gsl-histogram
%{_bindir}/gsl-randist
%{_libdir}/libgsl.so.28*
%{_libdir}/libgslcblas.so.0*
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*

%files devel
%{_bindir}/gsl-config
%{_libdir}/libgsl.so
%{_libdir}/libgslcblas.so
%{_libdir}/pkgconfig/gsl.pc
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/gsl.3*
%{_infodir}/gsl-ref.info*
%{_datadir}/aclocal/gsl.m4
%{_includedir}/gsl/

%changelog
%autochangelog
