# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           labwc
Version:        0.20.1
Release:        %autorelease
Summary:        A Wayland window-stacking compositor
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc
#!RemoteAsset:  sha256:2c95d8c19cc50ce0dd5cf3e412932ebb4d3353bc4a5d11e2405d124e6c77dcd2
Source0:        https://github.com/labwc/labwc/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

# Backport of upstream PR labwc/labwc#3656
# It can be removed in the next release, as it has been accepted upstream.
Patch0:         0001-output-force-initial-modeset-commit-on-new-output.patch

BuildOption(conf):  -Dxwayland=disabled

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libinput) >= 1.14
BuildRequires:  pkgconfig(libsfdo-basedir)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server) >= 0.19.0
BuildRequires:  pkgconfig(wlroots-0.20)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       xdg-desktop-portal-wlr
Requires:       xkeyboard-config

%description
Labwc is a wlroots-based window-stacking compositor for wayland, inspired by
openbox. It is light-weight and independent with a focus on simply stacking
windows well and rendering some window decorations.

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc NEWS.md README autostart environment menu.xml rc.xml rc.xml.all shutdown themerc
%license LICENSE
%{_bindir}/labwc
%{_bindir}/lab-sensible-terminal
%{_bindir}/labnag
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_datadir}/xdg-desktop-portal/labwc-portals.conf
%{_datadir}/wayland-sessions/labwc.desktop
%{_datadir}/icons/hicolor/*/*/labwc*.svg
%{_userunitdir}/labwc-session.target

%changelog
%autochangelog
