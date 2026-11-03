# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-exporter-otlp-common
%global pypi_name opentelemetry_exporter_otlp_common

Name:           python-%{srcname}
Version:        0.66b2
Release:        %autorelease
Summary:        OpenTelemetry OTLP HTTP export utilities
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
#!RemoteAsset:  sha256:06f5a9b88638e310efa1f1d206cdf6b75393e112aba4e174a963416192bd1028
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(opentelemetry-exporter-http-transport)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%pyproject_extras_subpkg -n %{name} http

%description
OpenTelemetry OTLP Utilities

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise OTLP metric aggregation, exporter metrics and HTTP client handling.
%py3_test_envvars %{__python3} -m unittest discover -s tests

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
