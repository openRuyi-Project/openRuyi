# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libqrtr-glib
Version:        1.2.2
Release:        %autorelease
Summary:        Qualcomm IPC Router protocol helper library
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/mobile-broadband/libqrtr-glib/
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  python3

%description
libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm
IPC Router) bus.

%package        devel
Summary:        Development files for the Qualcomm IPC Router protocol helper library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm
IPC Router) bus.

This package contains the header and pkg-config files for developing
applications using QRTR functionality.

%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS AUTHORS README.md
%{_libdir}/libqrtr-glib.so.*
%{_libdir}/girepository-1.0/Qrtr-1.0.typelib

%files devel
%{_includedir}/libqrtr-glib/
%{_libdir}/libqrtr-glib.so
%{_libdir}/pkgconfig/qrtr-glib.pc
%{_datadir}/gtk-doc/html/libqrtr-glib/
%{_datadir}/gir-1.0/Qrtr-1.0.gir

%changelog
%autochangelog
