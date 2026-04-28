# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-api
%global pypi_name opentelemetry_api

Name:           python-%{srcname}
Version:        1.41.0
Release:        %autorelease
Summary:        OpenTelemetry Python API
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
VCS:            git:https://github.com/open-telemetry/opentelemetry-python.git
#!RemoteAsset:  sha256:9421d911326ec12dee8bc933f7839090cad7a3f13fcfb0f9e82f8174dc003c09
Source:         https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Requires:       python3dist(importlib-metadata)
Requires:       python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
OpenTelemetry Python API provides the core API for OpenTelemetry tracing,
metrics, and logging in Python. It defines the interfaces and no-op
implementations that are used by the OpenTelemetry SDK and instrumentation
libraries.

%prep -a
# Relax importlib-metadata upper bound
sed -i 's/importlib-metadata >= 6.0, < 8.8.0/importlib-metadata >= 6.0/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
