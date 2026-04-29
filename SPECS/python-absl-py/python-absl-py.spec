# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname absl-py
%global pypi_name absl_py

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        Abseil Common Libraries (Python)
License:        Apache-2.0
URL:            https://github.com/abseil/abseil-py
#!RemoteAsset:  sha256:8c6af82722b35cf71e0f4d1d47dcaebfff286e27110a99fc359349b247dfb5d4
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l absl

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This repository is a collection of Python library code
for building Python applications. The code is collected from Google's
own Python code base, and has been extensively tested and used in production.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
