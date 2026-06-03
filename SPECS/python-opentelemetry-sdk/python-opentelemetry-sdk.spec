# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-sdk
%global pypi_name opentelemetry_sdk

Name:           python-%{srcname}
Version:        1.42.1
Release:        %autorelease
Summary:        OpenTelemetry Python SDK
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
#!RemoteAsset:  sha256:8c834e8f8c9ba4171d4ec843d0cb8a67e4c7394d3f9e9297e582cbd9456ddbf7
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
OpenTelemetry is an open source observability framework
for cloud native software. It provides a single set of APIs,
libraries, agents, and collector services to capture distributed
traces and metrics from your application.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
