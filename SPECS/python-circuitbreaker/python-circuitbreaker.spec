# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname circuitbreaker

Name:           python-%{srcname}
Version:        2.1.3
Release:        %autorelease
Summary:        Circuit breaker pattern implementation for Python
License:        BSD-3-Clause
URL:            https://github.com/fabfuel/circuitbreaker
#!RemoteAsset:  sha256:1a4baee510f7bea3c91b194dcce7c07805fe96c4423ed5594b75af438531d084
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Circuitbreaker provides a Python implementation of the circuit breaker
pattern for protecting calls to unreliable services.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
%autochangelog
