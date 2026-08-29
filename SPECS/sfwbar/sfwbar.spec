# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tarball_version 1.0_beta16.1

Name:           sfwbar
Version:        1.0~beta16.1
Release:        %autorelease
Summary:        S* Floating Window Bar
License:        GPL-3.0-only AND MIT
URL:            https://github.com/LBCrion/sfwbar
#!RemoteAsset:  sha256:98f3d77713a2e3a10fcb09c365c92fa96ab84bf157e59bd3f4d4d274ce0496e8
Source0:        https://github.com/LBCrion/sfwbar/archive/v%{tarball_version}/sfwbar-%{tarball_version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dmpd=disabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  python3dist(docutils)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbregistry)

Requires:       hicolor-icon-theme

%description
SFWBar (S* Floating Window Bar) is a flexible taskbar application for wayland
compositors.

%files
%doc README.md doc/ChangeLog
%license LICENSE
%{_bindir}/sfwbar
%{_datadir}/sfwbar/
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_libdir}/sfwbar/
%{_mandir}/man1/*.1*

%changelog
%autochangelog
