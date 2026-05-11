# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname lingua

Name:           python-%{srcname}
Version:        4.16.2
Release:        %autorelease
Summary:        Translation toolset
License:        BSD-3-Clause
URL:            https://github.com/wichert/lingua
VCS:            git:https://github.com/wichert/lingua.git
#!RemoteAsset:  sha256:b1e5cbbbecd40afd39ef3d4fcb40e4e3fc9b96bc0e043e708844a6d226ee54bd
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(chameleon)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(polib)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(chameleon)
Requires:       python3dist(click)
Requires:       python3dist(polib)

%description
Lingua is a package with tools to extract translatable texts from your code,
and to check existing translations. It replaces the use of the xgettext command
from gettext, or pybabel from Babel.

%prep -a
# Replace uv_build backend with hatchling (compatible, uv_build not packaged)
sed -i 's/requires = \["uv_build>=0.10.5,<0.11.0"\]/requires = ["hatchling"]/' pyproject.toml
sed -i 's/build-backend = "uv_build"/build-backend = "hatchling.build"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/polint
%{_bindir}/pot-create

%changelog
%autochangelog
