# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-exporter-otlp-proto-grpc
%global pypi_name opentelemetry_exporter_otlp_proto_grpc

Name:           python-%{srcname}
Version:        1.42.1
Release:        %autorelease
Summary:        OpenTelemetry OTLP protobuf gRPC exporter
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
VCS:            git:https://github.com/open-telemetry/opentelemetry-python.git
#!RemoteAsset:  sha256:975c4461f167dd8ed8857d68d3b6b25f3d272eab896f6a9470d0f5b90e2faf15
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(googleapis-common-protos)
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(opentelemetry-api)
BuildRequires:  python3dist(opentelemetry-exporter-otlp-proto-common)
BuildRequires:  python3dist(opentelemetry-proto)
BuildRequires:  python3dist(opentelemetry-sdk)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the OpenTelemetry Protocol (OTLP) exporter implementation
that sends protobuf-encoded telemetry data over gRPC.

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
