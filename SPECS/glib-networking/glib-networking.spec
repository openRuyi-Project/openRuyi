# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glib-networking
Version:        2.80.1
Release:        %autorelease
Summary:        Network-related GIO modules for GLib
License:        LGPL-2.1-or-later
URL:            https://www.gnome.org
VCS:            git:https://gitlab.gnome.org/GNOME/glib-networking.git
#!RemoteAsset
Source:         https://download.gnome.org/sources/glib-networking/2.80/glib-networking-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgnome_proxy=disabled

BuildRequires:  meson
BuildRequires:  ca-certificates-mozilla
BuildRequires:  dbus
BuildRequires:  gettext-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(systemd)

Requires:       ca-certificates-mozilla

%description
This package contains network-related GIO modules for GLib, providing
TLS (via GnuTLS) and proxy support (via libproxy).

%install -a
# Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*

%find_lang %{name} --generate-subpackages

%post
# TODO: When we have these macros, we should uncomment this.
# %%gio_module_post

%postun
# TODO: When we have these macros, we should uncomment this.
# %%gio_module_postun

%files -f %{name}.lang
%license COPYING
%doc NEWS README
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service
%{_libdir}/gio/modules/*.so
%{_libexecdir}/glib-pacrunner
%{_userunitdir}/glib-pacrunner.service

%changelog
%autochangelog
