# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xauth
Version:        1.1.5
Release:        %autorelease
Summary:        X authority file utility
License:        MIT-open-group
URL:            https://gitlab.freedesktop.org/xorg/app/xauth
VCS:            git:https://gitlab.freedesktop.org/xorg/app/xauth.git
#!RemoteAsset:  sha256:a4000e2f441facebf569026bedecc23ba262cc6927be52070abe0002625cfbe0
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  xtrans

%description
xauth is used to edit and display authorization information for connecting
to X servers.

%conf -p
autoreconf -fiv

%files
%doc README.md
%license COPYING
%{_bindir}/xauth
%{_mandir}/man1/xauth.1*

%changelog
%autochangelog
