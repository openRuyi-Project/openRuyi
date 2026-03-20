# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gexiv2
Version:        0.14.6
Release:        %autorelease
Summary:        Gexiv2 is a GObject-based wrapper around the Exiv2 library
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/Gexiv2
VCS:            git:https://gitlab.gnome.org/GNOME/gexiv2.git
#!RemoteAsset:  sha256:606c28aaae7b1f3ef5c8eabe5e7dffd7c5a1c866d25b7671fb847fe287a72b8b
Source0:        https://download.gnome.org/sources/gexiv2/0.14/gexiv2-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  python-pygobject
BuildRequires:  pkgconfig(exiv2) >= 0.14.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(python)

%description
libgexiv2 is a GObject-based wrapper around the Exiv2 library.
It makes the basic features of Exiv2 available to GNOME applications.

%package        devel
Summary:        Headers for developing programs that will use gexiv2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files needed for
developing with gexiv2.

%package     -n python-gexiv2
Summary:        Python bindings for gexiv2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-gexiv2 = %{version}-%{release}
%python_provide python3-gexiv2

%description -n python-gexiv2
This package contains the python bindings for gexiv2.

%files
%license COPYING
%{_libdir}/libgexiv2.so.2*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GExiv2-0.10.typelib

%files devel
%{_includedir}/gexiv2/
%{_libdir}/libgexiv2.so
%{_libdir}/pkgconfig/gexiv2.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GExiv2-0.10.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gexiv2.deps
%{_datadir}/vala/vapi/gexiv2.vapi

%files -n python-gexiv2
%pycached %{python3_sitelib}/gi/overrides/GExiv2.py

%changelog
%autochangelog
