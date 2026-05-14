# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond docs 0
# skip tests as some deps are not available yet.
%bcond tests 0

Name:           xdg-desktop-portal
Version:        1.20.3
Release:        %autorelease
Summary:        Portal frontend service to flatpak
License:        LGPL-2.1-or-later
URL:            https://github.com/flatpak/xdg-desktop-portal
#!RemoteAsset:  sha256:4bfb164937f59107eb1a3cc21abaa948d903c76f3b99fac210cea38ce1da9edc
Source0:        https://github.com/flatpak/xdg-desktop-portal/releases/download/%{version}/xdg-desktop-portal-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dman-pages=disabled
BuildOption(conf):  -Dflatpak-interfaces=disabled
BuildOption(conf):  -Dgeoclue=disabled
BuildOption(conf):  -Dtests=disabled
%if %{with tests}
BuildOption(conf):  -Dtests=enabled
%else
BuildOption(conf):  -Dtests=disabled
%endif
%if %{with docs}
BuildOption(conf):  -Ddocumentation=enabled
%else
BuildOption(conf):  -Ddocumentation=disabled
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros
BuildRequires:  bubblewrap
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
# not available yet
# BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
%if %{with tests}
BuildRequires:  pkgconfig(umockdev-1.0)
%endif
%if %{with docs}
BuildRequires:  python3dist(furo)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinxext-opengraph)
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  /usr/bin/rst2man
%endif

Requires:       dbus
Requires:       glib
Requires:       fuse3
# not available yet
# Requires:      geoclue2
Requires:       pipewire

%description
xdg-desktop-portal works by exposing a series of D-Bus interfaces known as
portals under a well-known name. The portal interfaces include APIs for
file access, opening URIs, printing and others.

%if %{without tests}
%check
%endif

%install -a
install -dm 755 %{buildroot}/%{_datadir}/xdg-desktop-portal/portals
install -dm 755 %{buildroot}/%{_pkgdocdir}
install -pm 644 README.md %{buildroot}/%{_pkgdocdir}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%post
%systemd_user_post xdg-desktop-portal.service
%systemd_user_post xdg-document-portal.service
%systemd_user_post xdg-permission-store.service

%preun
%systemd_user_preun xdg-desktop-portal.service
%systemd_user_preun xdg-document-portal.service
%systemd_user_preun xdg-permission-store.service

%files -f %{name}.lang
%doc %{_pkgdocdir}
%license COPYING
%{_datadir}/dbus-1/interfaces/org.freedesktop.host.portal.Registry.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.*.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.*.xml
%{_datadir}/dbus-1/services/org.freedesktop.portal.Desktop.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Documents.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%{_datadir}/xdg-desktop-portal/
%{_libexecdir}/xdg-desktop-portal
%{_libexecdir}/xdg-desktop-portal-rewrite-launchers
%{_libexecdir}/xdg-desktop-portal-validate-icon
%{_libexecdir}/xdg-desktop-portal-validate-sound
%{_libexecdir}/xdg-document-portal
%{_libexecdir}/xdg-permission-store
%{_userunitdir}/xdg-desktop-portal.service
%{_userunitdir}/xdg-desktop-portal-rewrite-launchers.service
%{_userunitdir}/xdg-document-portal.service
%{_userunitdir}/xdg-permission-store.service
%{_datadir}/pkgconfig/xdg-desktop-portal.pc

%changelog
%autochangelog
