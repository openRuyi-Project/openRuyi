# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname meson-python

Name:           python-%{srcname}
Version:        0.18.0
Release:        %autorelease
License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Summary:        Meson-based build backend for Python
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/meson_python-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l mesonpy +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  patchelf
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyproject-metadata)
BuildRequires:  meson

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

Requires:       meson
Requires:       ninja
Requires:       patchelf

%description
Meson-python is a PEP 517 build backend for Meson projects.

# XXX: %%pyproject_buildrequires no work with this package.
%generate_buildrequires

%files -f %{pyproject_files}

%changelog
%{?autochangelog}
