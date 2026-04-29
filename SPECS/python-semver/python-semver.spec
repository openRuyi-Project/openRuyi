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
#!RemoteAsset:  sha256:afc7d8c584a5ed0a11033af086e8af226a9c0b206f313e0301f8dd7b6b589602
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

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A Python module for semantic versioning. Simplifies comparing versions.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest

%files -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.txt
%{_bindir}/pysemver

%changelog
%autochangelog
