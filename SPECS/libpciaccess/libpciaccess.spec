# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpciaccess
Version:        0.18
Release:        %autorelease
Summary:        PCI access library
License:        HPND AND MIT
URL:            https://www.x.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libpciaccess.git
#!RemoteAsset
Source0:        https://www.x.org/archive/individual/lib/libpciaccess-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  util-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(zlib)

Requires:       hwdata

%description
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

%package devel
Summary:        Development files for the PCI access library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains the header files and development library for libpciaccess.

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libpciaccess.so.0*

%files devel
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc

%changelog
%autochangelog
