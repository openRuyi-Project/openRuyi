# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname absl-py
%global pypi_name absl_py

Name:           python-%{srcname}
Version:        2.3.1
Release:        %autorelease
Summary:        Abseil Python common libraries
License:        Apache-2.0
URL:            https://github.com/abseil/abseil-py
#!RemoteAsset:  sha256:a97820526f7fbfd2ec1bce83f3f25e3a14840dac0d8e02a0b71cd75db3f77fc9
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l absl

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling) >= 1.26
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
absl-py provides common utility libraries used by Abseil-based Python
projects.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
