# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           PackageKit
Version:        1.3.3
Release:        %autorelease
Summary:        Package management service
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND FSFAP
URL:            http://www.freedesktop.org/software/PackageKit/
VCS:            git:https://github.com/PackageKit/PackageKit
#!RemoteAsset:  sha256:d41d7bed865f827588e89727594d12a8059ed67fff50c7f323147dc11e7d0eb1
Source:         https://github.com/PackageKit/PackageKit/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    meson

# remove libdnf package.
Patch:          0001-remove-libdnf.patch

BuildOption(conf):  -Dgtk_doc=false
BuildOption(conf):  -Dman_pages=false
BuildOption(conf):  -Dgtk_module=false
BuildOption(conf):  -Dpython_backend=false
BuildOption(conf):  -Dpackaging_backend=dnf
BuildOption(conf):  -Dlocal_checkout=true
BuildOption(conf):  -Dgstreamer_plugin=false

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vala
BuildRequires:  libxslt
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdnf5)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  systemd
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(pangoft2)

Requires:       glib
Requires:       shared-mime-info
%{?systemd_requires}

%description
PackageKit is a D-Bus abstraction layer that allows the session user
to manage packages in a secure way using a cross-distro,
cross-architecture API.

%package        devel
Summary:        GLib Libraries and headers for PackageKit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
GLib headers and libraries for PackageKit.

%install -a
# Create cache dirs
mkdir -p %{buildroot}%{_localstatedir}/cache/PackageKit
mkdir -p %{buildroot}%{_localstatedir}/cache/app-info/{icons,xmls}

# GStreamer compatibility link
ln -s pk-gstreamer-install %{buildroot}%{_libexecdir}/gst-install-plugins-helper

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%check
# Skip tests in RPM build environment due to environment limitations

%post
%systemd_post packagekit-offline-update.service packagekit.service

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS NEWS
%dir %{_datadir}/PackageKit
%dir %{_sysconfdir}/PackageKit
%dir %{_localstatedir}/lib/PackageKit
%dir %{_localstatedir}/cache/app-info
%dir %{_localstatedir}/cache/app-info/icons
%dir %{_localstatedir}/cache/app-info/xmls
%dir %{_localstatedir}/cache/PackageKit
%{_datadir}/bash-completion/completions/pkcon
%dir %{_libdir}/packagekit-backend
%config(noreplace) %{_sysconfdir}/PackageKit/PackageKit.conf
%config(noreplace) %{_sysconfdir}/PackageKit/Vendor.conf
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/polkit-1/rules.d/*
%{_datadir}/PackageKit/pk-upgrade-distro.sh
%{_datadir}/PackageKit/helpers/test_spawn/search-name.sh
%{_datadir}/metainfo/org.freedesktop.packagekit.metainfo.xml
%{_libexecdir}/packagekitd
%{_libexecdir}/packagekit-direct
%{_bindir}/pkmon
%{_bindir}/pkcon
%{_libdir}/packagekit-backend/libpk_backend_dummy.so
%{_libdir}/packagekit-backend/libpk_backend_test_*.so
%ghost %verify(not md5 size mtime) %attr(0644,-,-) %{_localstatedir}/lib/PackageKit/transactions.db
%{_datadir}/dbus-1/system.d/*
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_unitdir}/packagekit-offline-update.service
%{_unitdir}/packagekit.service
%{_unitdir}/system-update.target.wants/
%{_libexecdir}/pk-*offline-update
%{_libdir}/*packagekit-glib2.so.*
%{_libdir}/girepository-1.0/PackageKitGlib-1.0.typelib
%config %{_sysconfdir}/cron.daily/packagekit-background.cron
%config(noreplace) %{_sysconfdir}/sysconfig/packagekit-background
%{_libexecdir}/gst-install-plugins-helper
%{_sysconfdir}/profile.d/*
%{_libexecdir}/pk-command-not-found
%config(noreplace) %{_sysconfdir}/PackageKit/CommandNotFound.conf
%{_libdir}/libdnf5/plugins/notify_packagekit.so
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/notify_packagekit.conf

%files devel
%{_libdir}/libpackagekit-glib2.so
%{_libdir}/pkgconfig/packagekit-glib2.pc
%dir %{_includedir}/PackageKit
%dir %{_includedir}/PackageKit/packagekit-glib2
%{_includedir}/PackageKit/packagekit-glib*/*.h
%{_datadir}/gir-1.0/PackageKitGlib-1.0.gir
%{_datadir}/vala/vapi/packagekit-glib2.vapi
%{_datadir}/vala/vapi/packagekit-glib2.deps

%changelog
%autochangelog
