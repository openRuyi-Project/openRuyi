# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-exporter-otlp
%global pypi_name opentelemetry_exporter_otlp

Name:           python-%{srcname}
Version:        1.42.1
Release:        %autorelease
Summary:        OpenTelemetry OTLP exporter convenience package
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
VCS:            git:https://github.com/open-telemetry/opentelemetry-python.git
#!RemoteAsset:  sha256:2d9ebaed714377a67d224d46795ddcc11d2c877fa5de35fda70b6f3b010729a9
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(opentelemetry-exporter-otlp-proto-grpc)
BuildRequires:  python3dist(opentelemetry-exporter-otlp-proto-http)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package is a convenience metapackage for installing the OpenTelemetry OTLP
exporters for both gRPC and HTTP transports.

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
