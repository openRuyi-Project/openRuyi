# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname async-timeout
%global pypi_name async_timeout

Name:           python-%{srcname}
Version:        5.0.1
Release:        %autorelease
Summary:        Timeout context manager for asyncio programs
License:        Apache-2.0
URL:            https://github.com/aio-libs/async-timeout
#!RemoteAsset:  sha256:d9321a7a3d5a6a5e187e824d2fa0793ce379a202935782d555d6e9d2735677d3
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
# for test
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Asyncio-compatible timeout context manager for Python programs.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Upstream pytest addopts enable coverage; clear them to run tests without pytest-cov.
%pytest -o "addopts=" -v tests/test_timeout.py

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
