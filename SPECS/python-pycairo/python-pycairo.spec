# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycairo

Name:           python-%{srcname}
Version:        1.29.0
Release:        %autorelease
Summary:        Python interface for cairo
License:        LGPL-2.1-only OR MPL-1.1
URL:            https://www.cairographics.org/pycairo
VCS:            git:https://github.com/pygobject/pycairo.git
#!RemoteAsset:  sha256:f3f7fde97325cae80224c09f12564ef58d0d0f655da0e3b040f5807bd5bd3142
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python bindings for the cairo library.

%package        devel
Summary:        Development files for embedding pycairo
Requires:       python3-%{srcname}%{?_isa} = %{version}-%{release}

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
%autochangelog
