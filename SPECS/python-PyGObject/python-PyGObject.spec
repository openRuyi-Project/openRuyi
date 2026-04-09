# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname PyGObject

# For some stupid reasons, we decided to name the package python-pygobject instead of PyGObject
# which is really bad. Like, wtf is this naming convention? It doesn't make any sense.
# We should really consider rename the package to PyGObject in the future. - 251
Name:           python-PyGObject
Version:        3.56.0
Release:        %autorelease
Summary:        Python bindings for GObject Introspection
License:        LGPL-2.1-or-later
URL:            https://pygobject.gnome.org/
VCS:            git:https://gitlab.gnome.org/GNOME/pygobject.git
#!RemoteAsset:  sha256:4fbb5bf47524e01026f8e309dd54233eb0f75f2281392c5bf0df5d9041cc7891
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/pygobject-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dpycairo=disabled

BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libffi)
# TODO: Add pycairo support in the future - 251
#BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  meson
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-gobject
Provides:       python3-gobject%{?_isa}
%python_provide python3-gobject

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package        devel
Summary:        Development files for embedding PyGObject introspection support
Requires:       python3-gobject%{?_isa} = %{version}-%{release}

%description    devel
This package contains files required to embed PyGObject introspection
support in other Python modules.

# Tests are disabled until Xwayland can run in mock
%check

%files
%doc NEWS
%license COPYING
#{python3_sitearch}/gi/_gi_cairo*.so
%dir %{python3_sitearch}/gi/
%{python3_sitearch}/gi/overrides/
%{python3_sitearch}/gi/repository/
%pycached %{python3_sitearch}/gi/*.py
%{python3_sitearch}/gi/_gi.*.so
%{python3_sitearch}/PyGObject-*.dist-info/

%files devel
%dir %{_includedir}/pygobject-3.0/
%{_includedir}/pygobject-3.0/pygobject.h
%{_includedir}/pygobject-3.0/pygobject-types.h
%{_libdir}/pkgconfig/pygobject-3.0.pc

%changelog
%autochangelog
