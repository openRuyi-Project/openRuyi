# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           guile
Version:        3.0.11
Release:        %autorelease
Summary:        GNU's Ubiquitous Intelligent Language for Extension
License:        GFDL-1.3-only AND GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.gnu.org/software/guile/
VCS:            git:https://codeberg.org/guile/guile.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/guile/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/guile/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig(libxcrypt)

%description
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs.

%package        devel
Summary:        GNU's Ubiquitous Intelligent Language for Extension
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(bdw-gc)
Requires:       pkgconfig(gmp)
Requires:       pkgconfig(ncurses)
Requires:       pkgconfig(readline)
Requires:       pkgconfig(libffi)
Requires:       libunistring-devel
Requires:       pkgconfig(libxcrypt)

%description    devel
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs.

%files
%license LICENSE COPYING*
%doc ABOUT-NLS AUTHORS ChangeLog GUILE-VERSION HACKING
%doc NEWS README THANKS
%{_bindir}/guile-tools
%{_bindir}/guild
%{_bindir}/guile
%{_libdir}/*.so.*
%{_libdir}/guile
%{_datadir}/guile
%{_mandir}/man1/guile.1*

%files devel
%{_bindir}/guile-snarf
%{_bindir}/guile-config
%{_includedir}/guile/*
%{_datadir}/aclocal/guile.m4
%{_infodir}/*.info*
%{_libdir}/libguile-*.so
%{_libdir}/pkgconfig/guile-*.pc

%changelog
%autochangelog
