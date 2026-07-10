# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-exporter-otlp-proto-common
%global pypi_name opentelemetry_exporter_otlp_proto_common

Name:           python-%{srcname}
Version:        1.42.1
Release:        %autorelease
Summary:        Common code for OpenTelemetry OTLP protobuf exporters
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
VCS:            git:https://github.com/open-telemetry/opentelemetry-python.git
#!RemoteAsset:  sha256:04f1f01fb597c4249dfcd7f8b861c902c2102369d376d9d346ff38de4469a2ee
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(opentelemetry-api)
BuildRequires:  python3dist(opentelemetry-proto)
BuildRequires:  python3dist(opentelemetry-sdk)
BuildRequires:  python3dist(opentelemetry-semantic-conventions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package contains shared helper code used by the OpenTelemetry OTLP
protobuf exporters for Python.

%prep -a
# Relax exact version pins on OpenTelemetry sibling packages.
sed -i -E 's/(opentelemetry-[[:alnum:]_.-]+)[[:space:]]*==[[:space:]]*/\1 >= /g' pyproject.toml
# Relax compatible-release pin on opentelemetry-sdk for repository integration.
sed -i -E 's/(opentelemetry-sdk)[[:space:]]*~=[[:space:]]*/\1 >= /g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
