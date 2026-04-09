# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           appstream-glib
Version:        0.8.3
Release:        %autorelease
Summary:        Library for AppStream metadata
License:        LGPL-2.1-or-later
URL:            http://people.freedesktop.org/~hughsient/appstream-glib/
VCS:            git:https://github.com/hughsie/appstream-glib
#!RemoteAsset:  sha256:84754064c560fca6e1ab151dc64354fc235a5798f016b91b38c9617253a8cf11
Source0:        http://people.freedesktop.org/~hughsient/appstream-glib/releases/appstream-glib-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddep11=false
BuildOption(conf):  -Dgtk-doc=false
BuildOption(conf):  -Dman=false
BuildOption(conf):  -Dbuilder=true

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gperf
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(rpm)

%description
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata.

%package        devel
Summary:        GLib Libraries and headers for appstream-glib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
GLib headers and libraries for appstream-glib.

%package        builder
Summary:        Library and command line tools for building AppStream metadata
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    builder
This library and command line tool is used for building AppStream metadata
from a directory of packages.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS NEWS
%{_libdir}/libappstream-glib.so.8*
%{_libdir}/girepository-1.0/*.typelib
%{_bindir}/appstream-util
%{_bindir}/appstream-compose
%{_datadir}/bash-completion/completions/appstream-util

%files devel
%{_libdir}/libappstream-glib.so
%{_libdir}/pkgconfig/appstream-glib.pc
%{_includedir}/libappstream-glib/
%{_datadir}/gir-1.0/AppStreamGlib-1.0.gir
%{_datadir}/aclocal/*.m4
%{_datadir}/installed-tests/appstream-glib/*.test
%{_datadir}/gettext/its/appdata.its
%{_datadir}/gettext/its/appdata.loc

%files builder
%license COPYING
%{_bindir}/appstream-builder
%{_datadir}/bash-completion/completions/appstream-builder
%{_libdir}/asb-plugins-*/

%changelog
%autochangelog
