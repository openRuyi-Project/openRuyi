# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname semver

Name:           python-%{srcname}
Version:        3.0.4
Release:        %autorelease
Summary:        Python helper for Semantic Versioning
License:        BSD-3-Clause
URL:            https://github.com/python-semver/python-semver
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Don't do coverage tests.
Patch0:         0001-Remove-cov-related-options.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A Python module for semantic versioning. Simplifies comparing versions.

%generate_buildrequires
%pyproject_buildrequires

%check
%pytest

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/pysemver

%changelog
%autochangelog
