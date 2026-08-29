# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fcitx5-gtk
Version:        5.1.6
Release:        %autorelease
Summary:        Gtk IM module and glib based dbus client library for fcitx5
License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5-gtk
#!RemoteAsset:  sha256:e5301bd55ba281cfcdf4cd30a30affea5b1ed31964954294f99ef56c9b7c4562
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5-gtk/fcitx5-gtk-%{version}.tar.zst
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_GTK2_IM_MODULE=OFF
BuildOption(conf):  -DENABLE_GTK4_IM_MODULE=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  ninja
BuildRequires:  cmake(fmt)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Gtk IM module and glib based dbus client library for fcitx5.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description    devel
Development files for %{name}.

%files
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libFcitx5GClient.so.5.*
%{_libdir}/libFcitx5GClient.so.2
%{_libdir}/girepository-1.0/FcitxG-1.0.typelib
%{_libdir}/gtk-3.0/*/immodules/im-fcitx5.so
%{_bindir}/fcitx5-gtk3-immodule-probing

%files devel
%{_includedir}/Fcitx5/GClient/
%{_libdir}/cmake/Fcitx5GClient
%{_libdir}/libFcitx5GClient.so
%{_libdir}/pkgconfig/Fcitx5GClient.pc
%{_datadir}/gir-1.0/

%changelog
%autochangelog
