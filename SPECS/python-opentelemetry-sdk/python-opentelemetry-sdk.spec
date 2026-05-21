# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-sdk
%global pypi_name opentelemetry_sdk

Name:           python-%{srcname}
Version:        1.42.0
Release:        %autorelease
Summary:        OpenTelemetry Python SDK
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
#!RemoteAsset:  sha256:2479e462cc69357825c2c847ce4a601bc1b17e1279aa7f80d3490f0ae614d0e5
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
