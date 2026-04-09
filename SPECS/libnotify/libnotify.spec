# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnotify
Version:        0.8.7
Release:        %autorelease
Summary:        Desktop notification library
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libnotify
#!RemoteAsset
Source:         https://download.gnome.org/sources/libnotify/0.8/libnotify-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dtests=false
BuildOption(conf):  -Dman=false
BuildOption(conf):  -Dgtk_doc=false
BuildOption(conf):  -Ddocbook_docs=disabled

BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires:       glib

%description
libnotify is a library for sending desktop notifications to a notification
daemon, as defined in the freedesktop.org Desktop Notifications spec.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files needed for
development of programs using libnotify.

%files
%license COPYING
%doc NEWS AUTHORS README.md
%{_bindir}/notify-send
%{_libdir}/libnotify.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Notify-0.7.typelib

%files devel
%dir %{_includedir}/libnotify
%{_includedir}/libnotify/*
%{_libdir}/libnotify.so
%{_libdir}/pkgconfig/libnotify.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Notify-0.7.gir

%changelog
%autochangelog
