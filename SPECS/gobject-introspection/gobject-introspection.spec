# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond    tests        0
%bcond    doc          0

%global major_version 1.86

Name:           gobject-introspection
Version:        %{major_version}.0
Release:        %autorelease
Summary:        Introspection system for GObject-based libraries
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://gi.readthedocs.io/
VCS:            git:https://gitlab.gnome.org/GNOME/gobject-introspection.git
#!RemoteAsset:  sha256:920d1a3fcedeadc32acff95c2e203b319039dd4b4a08dd1a2dfd283d19c0b9ae
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgtk_doc=%{?with_doc:true}%{!?with_doc:false}
BuildOption(conf):  -Ddoctool=%{?with_doc:enabled}%{!?with_doc:disabled}
BuildOption(conf):  -Dcairo=%{?with_tests:enabled}%{!?with_tests:disabled}

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  libffi-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(glib-2.0)
%if %{with tests}
BuildRequires:  pkgconfig(cairo-gobject)
%endif
%if %{with doc}
BuildRequires:  gtk-doc
BuildRequires:  python3dist(mako)
BuildRequires:  python3dist(markdown)
%endif

%description
GObject Introspection is a framework for generating and consuming API metadata
for GObject-based libraries. This package contains the core runtime library,
libgirepository, and the binary metadata (.typelib) files.

%package        devel
Summary:        The GObject Introspection development toolchain
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python(abi) = %{python3_version}
Requires:       pkgconfig(glib-2.0) >= 2.80.0
# The package uses distutils which is no longer part of Python 3.12+ standard library
# https://bugzilla.redhat.com/show_bug.cgi?id=2135406
Requires:       python3dist(setuptools)

%description    devel
This is the primary package for developers. It contains the essential
toolchain (g-ir-scanner, etc.), header files, and development metadata (.gir)
needed to generate introspection data for other GObject-based libraries.

%files
%license COPYING.LGPL
# The main package owns only the runtime library and the binary typelib files.
%{_libdir}/libgirepository-1.0.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%license COPYING COPYING.GPL
%doc NEWS README.rst
%{_bindir}/g-ir-*
%{_includedir}/gobject-introspection-1.0/
%{_libdir}/gobject-introspection/
%{_libdir}/libgirepository-1.0.so
%{_libdir}/pkgconfig/gobject-introspection-1.0.pc
%{_libdir}/pkgconfig/gobject-introspection-no-export-1.0.pc
%dir %{_datadir}/gir-1.0
# The XML .gir files are for development.
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gir-1.0/gir-1.2.rnc
%{_datadir}/gobject-introspection-1.0/
%{_datadir}/aclocal/introspection.m4
%{_mandir}/man1/g-ir-*.1*
%if %{with doc}
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gi/
%endif

%changelog
%autochangelog
