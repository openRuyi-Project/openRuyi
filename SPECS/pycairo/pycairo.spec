# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycairo

Name:           python-cairo
Version:        1.29.0
Release:        %autorelease
Summary:        Python interface for cairo
License:        LGPL-2.1-only OR MPL-1.1
URL:            https://www.cairographics.org/pycairo
VCS:            git:https://github.com/pygobject/pycairo.git
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-cairo
Provides:       python3-cairo%{?_isa}
%python_provide python3-cairo

%description
Python bindings for the cairo library.

%package        devel
Summary:        Development files for embedding pycairo
Requires:       python3-cairo%{?_isa} = %{version}-%{release}

%description    devel
This package contains files required to embed pycairo support
in other Python modules.

%files
%doc README.rst
%license COPYING*
%{python3_sitearch}/cairo/
%{python3_sitearch}/pycairo*.dist-info

%files devel
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc

%changelog
%{?autochangelog}
