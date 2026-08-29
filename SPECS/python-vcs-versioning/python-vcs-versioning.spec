# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname vcs-versioning
%global pypi_name vcs_versioning

Name:           python-vcs-versioning
Version:        1.1.1
Release:        %autorelease
Summary:        Manage Python package versions from VCS metadata
License:        MIT
URL:            https://github.com/pypa/setuptools-scm
#!RemoteAsset:  sha256:fabd75a3cab7dd8ac02fe24a3a9ba936bf258667b5a62ed468c9a1da0f5775bc
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
# Need pytest
BuildOption(check):  -e vcs_versioning.test_api

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(packaging) >= 20
BuildRequires:  python3dist(setuptools) >= 77.0.3

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
vcs-versioning manages Python package versions based on version control system
metadata.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{_bindir}/vcs-versioning

%changelog
%autochangelog
