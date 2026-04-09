# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libgusb
Version:        0.4.9
Release:        %autorelease
Summary:        GLib wrapper around libusb1
License:        LGPL-2.1-or-later
URL:            https://github.com/hughsie/libgusb
#!RemoteAsset
Source0:        https://github.com/hughsie/libgusb/releases/download/%{version}/libgusb-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddocs=false
BuildOption(conf):  -Dtests=false
BuildOption(conf):  -Dvapi=true

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  vala

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%files
%license COPYING
%{_libdir}/libgusb.so.*
%{_libdir}/girepository-1.0/GUsb-1.0.typelib
%{_bindir}/gusbcmd

%files devel
%{_includedir}/gusb-1/
%{_libdir}/libgusb.so
%{_libdir}/pkgconfig/gusb.pc
%{_datadir}/gir-1.0/GUsb-1.0.gir
%{_datadir}/vala/vapi/gusb.vapi
%{_datadir}/vala/vapi/gusb.deps

%changelog
%autochangelog
