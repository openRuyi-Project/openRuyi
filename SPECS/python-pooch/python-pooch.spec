# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pooch

Name:           python-%{srcname}
Version:        1.9.0
Release:        %autorelease
Summary:        A friend to fetch your data files
License:        BSD-3-Clause
URL:            https://github.com/fatiando/pooch
#!RemoteAsset:  sha256:de46729579b9857ffd3e741987a2f6d5e0e03219892c167c6578c0091fb511ed
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pooch manages your Python library's sample data files:
it automatically downloads and stores them in a local directory,
with support for versioning and corruption checks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
