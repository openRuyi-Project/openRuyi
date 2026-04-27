# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname prometheus-fastapi-instrumentator
%global pypi_name prometheus_fastapi_instrumentator

Name:           python-%{srcname}
Version:        7.1.0
Release:        %autorelease
Summary:        Instrument your FastAPI with Prometheus metrics
License:        ISC
URL:            https://github.com/trallnag/prometheus-fastapi-instrumentator
#!RemoteAsset:  sha256:be7cd61eeea4e5912aeccb4261c6631b3f227d8924542d79eaf5af3f439cbe5e
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(prometheus-client)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%prep -a
sed -i 's/starlette (>=0.30.0,<1.0.0)/starlette >= 0.30.0/g' pyproject.toml

%description
A configurable and modular Prometheus Instrumentator for your FastAPI.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
