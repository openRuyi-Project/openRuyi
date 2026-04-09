# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libqmi
Version:        1.36.0
Release:        %autorelease
Summary:        Qualcomm MSM Interface (QMI) modem protocol helper library
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/mobile-broadband/libqmi/
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/mobile-broadband/libqmi/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(mbim-glib)
BuildRequires:  pkgconfig(qrtr-glib)
BuildRequires:  python3
BuildRequires:  help2man

%description
libqmi is a glib-based library for talking to WWAN modems and devices
which speak the Qualcomm MSM Interface (QMI) protocol.

%package        devel
Summary:        Header files for adding QMI support to applications that use glib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libqmi is a glib-based library for talking to WWAN modems and devices
which speak the Qualcomm MSM Interface (QMI) protocol.

This package contains the header and pkg-config files for developing
applications using QMI functionality.

%files
%doc NEWS AUTHORS README.md
%license COPYING.LIB
%{_libdir}/libqmi-glib.so.*
%{_libdir}/girepository-1.0/Qmi-1.0.typelib
# tools
%{_bindir}/qmicli
%{_bindir}/qmi-network
%{_bindir}/qmi-firmware-update
%{_datadir}/bash-completion/completions/qmicli
%{_libexecdir}/qmi-proxy
%{_mandir}/man1/qmi-network.1*
%{_mandir}/man1/qmicli.1*
%{_mandir}/man1/qmi-firmware-update.1*

%files devel
%{_includedir}/libqmi-glib/
%{_libdir}/pkgconfig/qmi-glib.pc
%{_libdir}/libqmi-glib.so
%{_datadir}/gir-1.0/Qmi-1.0.gir

%changelog
%autochangelog
