# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpciaccess
Version:        0.18
Release:        %autorelease
Summary:        PCI access library
License:        HPND AND MIT
URL:            https://www.x.org/
#!RemoteAsset
Source0:        https://www.x.org/archive/individual/lib/libpciaccess-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  autoconf automake libtool pkgconfig util-macros
BuildRequires:  meson zlib-devel
Requires:       hwdata

%description
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

%package devel
Summary:        Development files for the PCI access library
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
This package contains the header files and development library for libpciaccess.

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libpciaccess.so.0*

%files devel
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc

%changelog
%{?autochangelog}
