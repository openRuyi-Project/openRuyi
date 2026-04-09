# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xrdb
Version:        1.2.2
Release:        %autorelease
Summary:        X server resource database utility
License:        MIT
URL:            https://gitlab.freedesktop.org/xorg/app/xrdb
#!RemoteAsset:  sha256:31f5fcab231b38f255b00b066cf7ea3b496df712c9eb2d0d50c670b63e5033f4
Source0:        https://www.x.org/pub/individual/app/xrdb-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)

%description
xrdb is used to get or set the contents of the RESOURCE_MANAGER property on
the root window of screen 0, or the SCREEN_RESOURCES property on the
root window of any or all screens, or everything combined.

%conf -p
autoreconf -fiv

%files
%license COPYING
%{_bindir}/xrdb
%{_mandir}/man1/xrdb.1*

%changelog
%autochangelog
