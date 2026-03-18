# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-semantic-conventions

Name:           python-%{srcname}
Version:        0.61b0
Release:        %autorelease
Summary:        OpenTelemetry Semantic Conventions
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/opentelemetry_semantic_conventions-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(opentelemetry-api)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
OpenTelemetry Semantic Conventions defines the standard attribute names and
values for OpenTelemetry, ensuring consistent telemetry data across different
languages and implementations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
