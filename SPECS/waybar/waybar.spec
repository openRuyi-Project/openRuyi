# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           waybar
Version:        0.15.0
Release:        %autorelease
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors
License:        MIT AND BSL-1.0 AND ISC
URL:            https://github.com/Alexays/Waybar
#!RemoteAsset:  sha256:21c2bbef88c40473c355003582f9331d2f9b8a01efdcce0935edfc5f6b023a3e
Source0:        https://github.com/Alexays/Waybar/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dsndio=disabled
BuildOption(conf):  -Dsystemd=enabled
BuildOption(conf):  -Dpipewire=enabled
BuildOption(conf):  -Dman-pages=enabled
BuildOption(conf):  -Ddbusmenu-gtk=disabled
BuildOption(conf):  -Dupower_glib=disabled
BuildOption(conf):  -Dmpris=disabled
BuildOption(conf):  -Dgps=disabled
BuildOption(conf):  -Dcava=disabled
BuildOption(conf):  -Djack=disabled
BuildOption(conf):  -Dwireplumber=disabled
BuildOption(conf):  -Dmpd=disabled
BuildOption(conf):  -Dtests=enabled

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  scdoc
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(xkbregistry)
# for tests
BuildRequires:  pkgconfig(catch2)

%description
Waybar is a highly customizable Wayland bar for Sway and Wlroots based
compositors.

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/waybar
%config(noreplace) %{_sysconfdir}/xdg/waybar/config.jsonc
%config(noreplace) %{_sysconfdir}/xdg/waybar/style.css
%{_bindir}/waybar
%{_userunitdir}/waybar.service
%{_mandir}/man5/waybar*

%changelog
%{?autochangelog}
