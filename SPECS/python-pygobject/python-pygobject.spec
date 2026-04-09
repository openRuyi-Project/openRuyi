# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-pygobject
%define major_version 3
%define minor_version 54
%define patch_version 2
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        %autorelease
Summary:        Python bindings for GObject Introspection
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/PyGObject
#!RemoteAsset
Source0:        https://download.gnome.org/sources/pygobject/%{major_version}.%{minor_version}/pygobject-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dpython=%{__python3}
BuildOption(conf):  -Dpycairo=disabled

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package -n python3-pygobject
Summary:        Python 3 bindings for GObject Introspection

%description -n python3-pygobject
The python3-gobject package provides a convenient wrapper for the GObject
library and and other libraries that are compatible with GObject Introspection,
for use in Python 3 programs.


%package     -n python3-pygobject-devel
Summary:        Development files for embedding PyGObject introspection support
Requires:       python3-pygobject
Requires:       gobject-introspection-devel

%description -n python3-pygobject-devel
This package contains files required to embed PyGObject

%files -n python3-pygobject
%license COPYING
%doc NEWS
%dir %{python3_sitearch}/gi/
%{python3_sitearch}/gi/overrides/
%{python3_sitearch}/gi/repository/
%pycached %{python3_sitearch}/gi/*.py
%{python3_sitearch}/gi/_gi.*.so
%{python3_sitearch}/PyGObject-*.dist-info/
%{python3_sitearch}/pygtkcompat/

%files -n python3-pygobject-devel
%dir %{_includedir}/pygobject-3.0/
%{_includedir}/pygobject-3.0/pygobject.h
%{_libdir}/pkgconfig/pygobject-3.0.pc

%changelog
%autochangelog
