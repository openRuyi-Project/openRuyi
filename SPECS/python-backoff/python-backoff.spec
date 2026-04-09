# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname backoff

Name:           python-%{srcname}
Version:        2.2.1
Release:        %autorelease
Summary:        Python library providing function decorators for configurable backoff and retry
License:        MIT
URL:            https://github.com/litl/backoff
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pytest
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This module provides function decorators which can be used to wrap
a function such that it will be retried until some condition is met.
It is meant to be of use when accessing unreliable resources with the
potential for intermittent failures i.e. network resources and external
APIs. Somewhat more generally, it may also be of use for dynamically
polling resources for externally generated content.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
