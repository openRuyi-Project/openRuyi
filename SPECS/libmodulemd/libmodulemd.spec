# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmodulemd
Version:        2.15.2
Release:        %autorelease
Summary:        Module metadata manipulation library
License:        MIT
URL:            https://github.com/fedora-modularity/libmodulemd
#!RemoteAsset:  sha256:6fb926e270ba44d1981d1abadaa6728c5e357636eee3b3bb533e95b92d104970
Source0:        %{url}/releases/download/%{version}/modulemd-%{version}.tar.xz
BuildSystem:    meson

Patch0:         0001-tests-Adapt-to-glib-2.87.0.patch
Patch1:         0002-tests-Adapt-to-pygobject-3.55.0.patch

BuildOption(conf):  -Drpmio=enabled
BuildOption(conf):  -Dskip_introspection=false
BuildOption(conf):  -Dtest_installed_lib=false
BuildOption(conf):  -Dwith_docs=false
BuildOption(conf):  -Dwith_manpages=enabled

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(yaml-0.1)
# doc gen tool is disabled to make this pkg usable ASAP
#BuildRequires:  pkgconfig(gtk-doc)
#BuildRequires:  glib2-doc
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pygobject)

%description
C library for manipulating module metadata files.
See https://github.com/fedora-modularity/libmodulemd/blob/main/README.md for
more details.

%package     -n python-%{name}
Summary:        Python bindings for %{name}
Provides:       python3-%{name} = %{version}-%{release}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3dist(pygobject)
Requires:       python3dist(six)

%description -n python-%{name}
Python bindings for %{name}.

%package        devel
Summary:        Development files for libmodulemd
Requires:       libmodulemd

%description    devel
Development files for %{name}.

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/modulemd-validator
%{_mandir}/man1/modulemd-validator.1*
%{_libdir}/libmodulemd.so.2*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Modulemd-2.0.typelib

%files devel
%{_libdir}/libmodulemd.so
%{_libdir}/pkgconfig/modulemd-2.0.pc
%{_includedir}/modulemd-2.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Modulemd-2.0.gir

%files -n python-%{name}
%{python3_sitearch}/gi/overrides/

%changelog
%autochangelog
