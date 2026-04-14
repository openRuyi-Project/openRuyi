# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-semantic-conventions
%global pypi_name opentelemetry_semantic_conventions

Name:           python-%{srcname}
Version:        0.62b0
Release:        %autorelease
Summary:        OpenTelemetry Semantic Conventions
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
VCS:            git:https://github.com/open-telemetry/opentelemetry-python.git
#!RemoteAsset:  sha256:cbfb3c8fc259575cf68a6e1b94083cc35adc4a6b06e8cf431efa0d62606c0097
Source:         https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Requires:       python3dist(opentelemetry-api)
Requires:       python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the OpenTelemetry Semantic Conventions for Python,
a set of well-defined attribute keys and values for common telemetry concepts.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
