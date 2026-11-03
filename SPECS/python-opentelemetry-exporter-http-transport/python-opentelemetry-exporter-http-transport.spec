# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-exporter-http-transport
%global pypi_name opentelemetry_exporter_http_transport

Name:           python-%{srcname}
Version:        0.66b2
Release:        %autorelease
Summary:        OpenTelemetry Exporters HTTP transport
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
#!RemoteAsset:  sha256:66d6ed810a515432c8891da9a834464332fd70badeca45bdeeae81b4280c903b
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(urllib3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%pyproject_extras_subpkg -n %{name} requests
%pyproject_extras_subpkg -n %{name} urllib3

%description
OpenTelemetry Exporters HTTP Transport

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Transport discovery covers both supported backends. Their mocked HTTP suites require mocket.
%py3_test_envvars %{__python3} -m unittest discover -s tests -p test_load_transport.py

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
