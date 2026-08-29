# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyproject-api
%global pypi_name pyproject_api

Name:           python-%{srcname}
Version:        1.10.0
Release:        %autorelease
Summary:        API to interact with the python pyproject.toml based projects
License:        MIT
URL:            https://pyproject-api.readthedocs.io/latest/
#!RemoteAsset:  sha256:40c6f2d82eebdc4afee61c773ed208c04c19db4c4a60d97f8d7be3ebc0bbb330
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pyproject_api

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
API to interact with the python pyproject.toml based projects.

%prep -a
# Remove unneeded testing deps
sed -i "/covdefaults/d;/pytest-cov/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x testing

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
