# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           font-util
Version:        1.4.2
Release:        %autorelease
Summary:        X.Org font package creation/installation utilities
License:        MIT
URL:            https://www.x.org/wiki/
VCS:            git:https://gitlab.freedesktop.org/xorg/font/util
#!RemoteAsset:  sha256:02e4f8afdcf03cc8372ca9c37aa104b1e36b47722dbc79531be08f0a4c622999
Source0:        https://xorg.freedesktop.org/archive/individual/font/%{name}-%{version}.tar.xz
#!RemoteAsset:  sha256:7b29d916b6bebda78fe05d9df9c6d68d6cc4df0df40652a61f5f226fb697b22e
Source1:        https://xorg.freedesktop.org/archive/individual/font/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --with-fontrootdir=%{_datadir}/fonts

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(xorg-macros)

%description
This package provides utilities for X.Org font package creation/installation.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/bdftruncate
%{_bindir}/ucs2any
%{_mandir}/man1/bdftruncate.1%{?ext_man}
%{_mandir}/man1/ucs2any.1%{?ext_man}
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/fontutil.m4
%{_datadir}/fonts/util/
%{_libdir}/pkgconfig/fontutil.pc

%changelog
%autochangelog
