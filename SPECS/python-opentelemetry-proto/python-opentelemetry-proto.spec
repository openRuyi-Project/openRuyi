# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-proto
%global pypi_name opentelemetry_proto

Name:           python-%{srcname}
Version:        1.42.1
Release:        %autorelease
Summary:        OpenTelemetry Python protobuf bindings
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
VCS:            git:https://github.com/open-telemetry/opentelemetry-python.git
#!RemoteAsset:  sha256:c6a51e6b4f05ae63565f3a113217f3d2bfaec68f78c02d7a6c85f9010d1cfca6
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(protobuf)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides generated Python protobuf bindings for the OpenTelemetry
protocol. It is shared by OpenTelemetry exporters and other OTLP components.

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
