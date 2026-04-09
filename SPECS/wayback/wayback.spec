# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wayback
Version:        0.3
Release:        %autorelease
Summary:        X11 compatibility layer built on wlroots and Xwayland
License:        MIT
URL:            https://gitlab.freedesktop.org/wayback/wayback
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/wayback/wayback/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(scdoc)

Requires:       Xwayland

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%{_bindir}/Xwayback
%{_bindir}/wayback-*
%{_libexecdir}/wayback-*
%{_mandir}/man1/*wayback*.1*

%changelog
%autochangelog
