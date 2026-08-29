# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-dependency
%global pypi_name pytest_dependency

Name:           python-%{srcname}
Version:        0.6.1
Release:        %autorelease
Summary:        Manage dependencies between pytest tests
License:        Apache-2.0
URL:            https://github.com/RKrahl/pytest-dependency
VCS:            git:https://github.com/RKrahl/pytest-dependency.git
#!RemoteAsset:  sha256:246c24d2a5fc743a942cec4408853640e56a05ba58d46e5b213a1d4b738a2464
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pytest_dependency

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pytest-dependency manages dependencies between tests. It can skip tests whose
prerequisites failed or were skipped during the same test run.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt

%changelog
%autochangelog
