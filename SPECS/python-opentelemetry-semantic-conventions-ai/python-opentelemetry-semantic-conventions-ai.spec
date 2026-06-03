# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-semantic-conventions-ai
%global pypi_name opentelemetry_semantic_conventions_ai

Name:           python-%{srcname}
Version:        0.5.1
Release:        %autorelease
Summary:        OpenTelemetry Semantic Conventions Extension for Large Language Models
License:        Apache-2.0
URL:            https://github.com/traceloop/openllmetry-python
#!RemoteAsset:  sha256:153906200d8c1d2f8e09bd78dbef526916023de85ac3dab35912bfafb69ff04c
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(opentelemetry-sdk)
BuildRequires:  python3dist(opentelemetry-semantic-conventions)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides OpenTelemetry Semantic Conventions extensions for
Large Language Models (LLMs), defining well-known attribute keys and values
for tracing LLM interactions.

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
