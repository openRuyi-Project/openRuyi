# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           isl
Version:        0.27
Release:        %autorelease
Summary:        Integer Set Library
License:        MIT
URL:            https://libisl.sourceforge.io/
VCS:            git:https://repo.or.cz/isl.git
#!RemoteAsset
Source:         https://libisl.sourceforge.io/isl-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig

%description
ISL is a library for manipulating sets and relations of integer points
bounded by linear constraints.
It is used by Cloog and the GCC Graphite optimization framework.

%package        devel
Summary:        Development tools for ISL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development tools and headers for the ISL.

%check
%make_build check

%install -a
rm -f  %{buildroot}%{_libdir}/libisl.so.*-gdb.py

%files
%{_libdir}/libisl.so.*

%files devel
%{_includedir}/isl
%{_libdir}/libisl.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
