# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gtk-doc
Version:        1.35.1
Release:        %autorelease
Summary:        API documentation generation tool for GTK+ and GNOME
License:        GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later
URL:            https://gitlab.gnome.org/GNOME/gtk-doc/
#!RemoteAsset:  sha256:611c9f24edd6d88a8ae9a79d73ab0dc63c89b81e90ecc31d6b9005c5f05b25e2
Source:         http://download.gnome.org/sources/gtk-doc/1.35/gtk-doc-%{version}.tar.xz
BuildSystem:    meson

# from https://gitlab.gnome.org/GNOME/gtk-doc/-/merge_requests/74
Patch0:         gtk-doc-mkhtml-test-fix.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(parameterized)
BuildRequires:  itstool
BuildRequires:  docbook-utils
BuildRequires:  libxslt
BuildRequires:  docbook-xsl

Requires:       docbook-utils
Requires:       libxslt
Requires:       docbook-xsl
Requires:       python3dist(pygments)
Requires:       python3dist(lxml)
Requires:       cmake-filesystem

%description
gtk-doc is a tool for generating API reference documentation.
It is used for generating the documentation for GTK+, GLib
and GNOME.

%prep -a
mv doc/README doc/README.docs

%install -a
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gtk-doc/

%files
%license COPYING COPYING-DOCS
%doc AUTHORS README doc/* examples
%{_bindir}/*
%{_datadir}/aclocal/gtk-doc.m4
%{_datadir}/gtk-doc/
%{_datadir}/pkgconfig/gtk-doc.pc
%{_datadir}/help/*/gtk-doc-manual/
%{_libdir}/cmake/GtkDoc/

%changelog
%autochangelog
