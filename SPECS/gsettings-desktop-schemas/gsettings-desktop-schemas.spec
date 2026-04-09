# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gsettings-desktop-schemas
Version:        49.1
Release:        %autorelease
Summary:        A collection of GSettings schemas
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas
#!RemoteAsset:  sha256:777a7f83d5e5a8076b9bf809cb24101b1b1ba9c230235e3c3de8e13968ed0e63
Source0:        https://download.gnome.org/sources/gsettings-desktop-schemas/49/gsettings-desktop-schemas-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
gsettings-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --with-gnome --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc AUTHORS MAINTAINERS NEWS README
%{_datadir}/glib-2.0/schemas/*
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gsettings-desktop-schemas.convert
%{_datadir}/GConf/gsettings/wm-schemas.convert
%{_libdir}/girepository-1.0/GDesktopEnums-3.0.typelib

%files devel
%doc HACKING
%{_includedir}/*
%{_datadir}/pkgconfig/*
%{_datadir}/gir-1.0/GDesktopEnums-3.0.gir

%changelog
%autochangelog
