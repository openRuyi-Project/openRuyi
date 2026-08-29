# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname importlib-metadata
%global pypi_name importlib_metadata

Name:           python-%{srcname}
Version:        9.0.0
Release:        %autorelease
Summary:        Library to access the metadata for a Python package
License:        Apache-2.0
URL:            https://github.com/python/importlib_metadata
#!RemoteAsset:  sha256:a4f57ab599e6a2e3016d7595cfd72eb4661a5106e787a95bcc90c7105b831efc
Source:         https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(coherent-licensed)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(zipp)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Library to access the metadata for a Python package.
This package supplies third-party access to the functionality
of importlib.metadata including improvements added to subsequent
Python versions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
