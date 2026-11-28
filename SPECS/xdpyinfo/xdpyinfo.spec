# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xdpyinfo
Version:        1.4.0
Release:        %autorelease
Summary:        Display information utility for X
License:        MIT-open-group
URL:            https://gitlab.freedesktop.org/xorg/app/xdpyinfo
VCS:            git:https://gitlab.freedesktop.org/xorg/app/xdpyinfo.git
#!RemoteAsset:  sha256:dc1de6e6e091ed46c4837b0ae9811e8182f7be0d2af638cab3e530ff081a48b6
Source:         https://www.x.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildSystem:    meson

# libXxf86dga is not packaged
BuildOption(conf):  -Ddga=disabled
BuildOption(conf):  -Ddmx=disabled
BuildOption(conf):  -Dxf86misc=disabled
BuildOption(conf):  -Dxinerama=enabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpresent)
BuildRequires:  pkgconfig(xproto) >= 7.0.22
BuildRequires:  pkgconfig(xrandr) >= 1.2
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86vm)

%description
xdpyinfo is a utility for displaying information about an X server.
It is used to examine the capabilities of a server, the predefined
values for various parameters used in communicating between clients
and the server, and the different types of screens, visuals, and X11
protocol extensions that are available.

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/xdpyinfo
%{_mandir}/man1/xdpyinfo.1*

%changelog
%autochangelog
