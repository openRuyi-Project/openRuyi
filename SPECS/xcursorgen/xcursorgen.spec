# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcursorgen
Version:        1.0.9
Release:        %autorelease
Summary:        Prepare X11 cursor sets for use with libXcursor
License:        HPND-sell-variant
URL:            https://gitlab.freedesktop.org/xorg/app/xcursorgen
#!RemoteAsset:  sha256:0cc9e156ac84ca16ea902710af35e0faffa51d13797071e3b4b6cc7cbd493bbc
Source0:        https://www.x.org/pub/individual/app/xcursorgen-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
xcursorgen prepares X11 cursor sets for use with libXcursor.

%conf -p
autoreconf -fiv

%files
%license COPYING
%{_bindir}/xcursorgen
%{_mandir}/man1/xcursorgen.1*

%changelog
%autochangelog
