# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           json-glib
Version:        1.10.8
Release:        %autorelease
Summary:        Library for JavaScript Object Notation (JSON) format
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/JsonGlib
VCS:            git:https://gitlab.gnome.org/GNOME/json-glib
#!RemoteAsset:  sha256:55c5c141a564245b8f8fbe7698663c87a45a7333c2a2c56f06f811ab73b212dd
Source:         https://download.gnome.org/sources/json-glib/1.10/json-glib-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddocumentation=disabled
BuildOption(conf):  -Dman=true
BuildOption(conf):  -Dtests=false

BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  gi-docgen
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  python3dist(docutils)

%description
json-glib is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.

%package        devel
Summary:        Development files and tools for json-glib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, documentation, and tools
needed to develop applications that use the json-glib library.

%install -a
# Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang json-glib-1.0 --generate-subpackages

%files -f json-glib-1.0.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS README.md
%{_libdir}/libjson-glib-1.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Json-1.0.typelib

%files devel
%{_includedir}/json-glib-1.0/json-glib/
%{_libdir}/libjson-glib-1.0.so
%{_libdir}/pkgconfig/json-glib-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Json-1.0.gir
%{_bindir}/json-glib-format
%{_bindir}/json-glib-validate
%{_mandir}/man1/json-glib-format.1*
%{_mandir}/man1/json-glib-validate.1*

%changelog
%autochangelog
