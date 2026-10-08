# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gcab
Version:        1.6
Release:        %autorelease
Summary:        Cabinet file library and tool
License:        LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gcab
VCS:            git:https://gitlab.gnome.org/GNOME/gcab.git
#!RemoteAsset:  sha256:cda7b2cbf3967ff9c48e75afb86ee683d98ad8fb2d9a4a966a9e10cfdb349886
Source0:        https://gitlab.gnome.org/GNOME/gcab/-/archive/v%{version}/gcab-v%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  vala
BuildRequires:  glib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  zlib-devel
BuildRequires:  meson
BuildRequires:  git

Requires:       libgcab1

%description
gcab is a tool to manipulate Cabinet archive.

%package -n libgcab1
Summary:        Library to create Cabinet archives

%description -n libgcab1
libgcab is a library to manipulate Cabinet archive using GIO/GObject.

%package -n libgcab1-devel
Summary:        Development files to create Cabinet archives
Requires:       libgcab1
Requires:       glib-devel
Requires:       pkgconfig

%description -n libgcab1-devel
libgcab is a library to manipulate Cabinet archive.

Libraries, includes, etc. to compile with the gcab library.

%files
%doc COPYING NEWS
%{_bindir}/gcab
%{_mandir}/man1/gcab.1*
%{_datadir}/locale/*/LC_MESSAGES/gcab.mo

%files -n libgcab1
%doc COPYING NEWS
%{_libdir}/girepository-1.0/GCab-1.0.typelib
%{_libdir}/libgcab-1.0.so.*

%files -n libgcab1-devel
%{_datadir}/gir-1.0/GCab-1.0.gir
%{_datadir}/gtk-doc/html/gcab/*
%{_datadir}/vala/vapi/libgcab-1.0.vapi
%{_datadir}/vala/vapi/libgcab-1.0.deps
%{_includedir}/libgcab-1.0/*
%{_libdir}/libgcab-1.0.so
%{_libdir}/pkgconfig/libgcab-1.0.pc

%changelog
%autochangelog
