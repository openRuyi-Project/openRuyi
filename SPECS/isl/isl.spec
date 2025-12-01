# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define islsover 23
Name:           isl
Version:        0.27
Release:        %autorelease
Summary:        Integer Set Library
License:        MIT
URL:            https://libisl.sourceforge.io/
#!RemoteAsset
Source:         https://libisl.sourceforge.io/isl-%{version}.tar.xz
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig

BuildSystem:    autotools
BuildOption(conf): --disable-static

%description
ISL is a library for manipulating sets and relations of integer points
bounded by linear constraints.
It is used by Cloog and the GCC Graphite optimization framework.

%package devel
Summary:        Development tools for ISL
Requires:       libisl%{islsover} = %{version}-%{release}

%description devel
Development tools and headers for the ISL.

%package -n libisl%{islsover}
Summary:        The ISL shared library

%description -n libisl%{islsover}
The shared library for the ISL.

ISL is a library for manipulating sets and relations of integer points
bounded by linear constraints.

%check
%make_build check

%install -a
rm -f  %{buildroot}%{_libdir}/libisl.so.*-gdb.py

%files -n libisl%{islsover}
%{_libdir}/libisl.so.%{islsover}*

%files devel
%{_includedir}/isl
%{_libdir}/libisl.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%{?autochangelog}
