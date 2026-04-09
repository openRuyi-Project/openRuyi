# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xdg-desktop-portal-wlr
Version:        0.8.1
Release:        %autorelease
Summary:        xdg-desktop-portal backend for wlroots
License:        MIT
URL:            https://github.com/emersion/xdg-desktop-portal-wlr
#!RemoteAsset
Source0:        https://github.com/emersion/xdg-desktop-portal-wlr/archive/refs/tags/v%{version}.tar.gz
Source1:        wlroots-portals.conf
BuildSystem:    meson

BuildOption(conf):  -Dsd-bus-provider=libsystemd

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-scanner)

Requires:       dbus
Requires:       xdg-desktop-portal

%description
This project adds support for the screenshot, screencast, and remote-desktop
xdg-desktop-portal interfaces for wlroots based compositors (like sway, labwc).

%install -a
install -D -p -m 644 %{SOURCE1} \
    %{buildroot}%{_datadir}/xdg-desktop-portal/wlroots-portals.conf

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md contrib/config.sample
%{_libexecdir}/xdg-desktop-portal-wlr
%{_mandir}/man5/xdg-desktop-portal-wlr.5*
%{_datadir}/xdg-desktop-portal/portals/wlr.portal
%{_datadir}/xdg-desktop-portal/wlroots-portals.conf
%{_datadir}/dbus-1/services/*.service
%{_userunitdir}/xdg-desktop-portal-wlr.service

%changelog
%autochangelog
