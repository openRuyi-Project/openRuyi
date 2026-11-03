# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-api
%global pypi_name opentelemetry_api

Name:           python-%{srcname}
# Update with python-opentelemetry-semantic-conventions - 251
Version:        1.45.2
Release:        %autorelease
Summary:        OpenTelemetry Python API
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
VCS:            git:https://github.com/open-telemetry/opentelemetry-python.git
#!RemoteAsset:  sha256:d7b0008e21e5fd61cbe7a7f34ca3b6905a78ab677d9bc395e299359c75cda6b4
Source:         https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)

Requires:       python3dist(typing-extensions) >= 4.5

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
OpenTelemetry Python API provides the core API for OpenTelemetry tracing,
metrics, and logging in Python. It defines the interfaces and no-op
implementations that are used by the OpenTelemetry SDK and instrumentation
libraries.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
