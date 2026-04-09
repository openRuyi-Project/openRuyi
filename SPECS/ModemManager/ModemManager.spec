# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ModemManager
Version:        1.24.2
Release:        %autorelease
Summary:        Mobile broadband modem management service
License:        GPL-2.0-or-later
URL:            https://modemmanager.org/
VCS:            git:https://gitlab.freedesktop.org/mobile-broadband/ModemManager
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/archive/%{version}/downloads/%{name}-%{version}.tar.gz
BuildSystem:    meson

%ifarch riscv64
# PTY/termios ioctls are not reliably emulated in qemu-user
Patch2000:      2000-Skip-tests-on-riscv64.patch
%endif

BuildOption(conf):  -Ddist_version='"%{version}-%{release}"'
BuildOption(conf):  -Ddbus_policy_dir=%{_datadir}/dbus-1/system.d
BuildOption(conf):  -Dsystemdsystemunitdir=%{_unitdir}
BuildOption(conf):  -Dvapi=true
BuildOption(conf):  -Dpolkit=permissive

BuildRequires:  meson
BuildRequires:  dbus-daemon
BuildRequires:  libxslt
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mbim-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(qmi-glib)
BuildRequires:  pkgconfig(qrtr-glib)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  vala
# Tests
BuildRequires:  python3-pygobject
BuildRequires:  python3-dbus

%description
The ModemManager service manages WWAN modems and provides a consistent API for
interacting with these devices to client applications.

%package        devel
Summary:        Libraries and headers for adding ModemManager support to applications
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains various headers for accessing some ModemManager functionality
from applications.

%package     -n libmm-glib
Summary:        Glib bindings for the modem handling DBus interface

%description -n libmm-glib
DBus interface for modem handling. Provides a standard abstracted API
(over DBus) to communicate with all sorts of modems (landline, GSM,
CDMA).

%install -a
%find_lang %{name} --generate-subpackages

%post
%systemd_post ModemManager.service

%preun
%systemd_preun ModemManager.service

%postun
%systemd_postun ModemManager.service

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/mmcli
%{_sbindir}/ModemManager
%{_datadir}/dbus-1/system.d/org.freedesktop.ModemManager1.conf
%{_libdir}/ModemManager/
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.ModemManager1.service
%{_datadir}/icons/hicolor/*/*/ModemManager.png
%{_datadir}/polkit-1/actions/org.freedesktop.ModemManager1.policy
%{_datadir}/ModemManager
%{_prefix}/lib/udev/rules.d/*-mm-*.rules
%{_unitdir}/ModemManager.service
%{_datadir}/bash-completion/
%{_mandir}/man1/mmcli.1*
%{_mandir}/man8/ModemManager.8*

%files devel
%{_includedir}/ModemManager/
%{_libdir}/pkgconfig/ModemManager.pc
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/vala/vapi/libmm-glib.*

%files -n libmm-glib
%{_libdir}/libmm-glib.so
# We make an exception here
%{_libdir}/libmm-glib.so.*
%dir %{_includedir}/libmm-glib
%{_includedir}/libmm-glib/*.h
%{_libdir}/pkgconfig/mm-glib.pc
%{_datadir}/gir-1.0/*.gir
%{_libdir}/girepository-1.0/*.typelib

%changelog
%autochangelog
