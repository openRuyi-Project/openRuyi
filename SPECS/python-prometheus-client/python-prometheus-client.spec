# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname prometheus-client
%global pypi_name prometheus_client

Name:           python-%{srcname}
Version:        0.25.0
Release:        %autorelease
Summary:        Python client for the Prometheus monitoring system
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/prometheus/client_python
VCS:            git:https://github.com/prometheus/client_python.git
#!RemoteAsset:  sha256:5e373b75c31afb3c86f1a52fa1ad470c9aace18082d39ec0d2f918d11cc9ba28
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
BuildOption(check):  -e "%{pypi_name}.twisted*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(django)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
prometheus-client is the official Python client library for Prometheus. It
provides metric types, a default registry, and an HTTP endpoint for scraping.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE NOTICE
%doc README.md

%changelog
%autochangelog
