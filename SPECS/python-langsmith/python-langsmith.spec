# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langsmith

Name:           python-%{srcname}
Version:        0.8.8
Release:        %autorelease
Summary:        Client library for the LangSmith platform
License:        MIT
URL:            https://smith.langchain.com/
VCS:            git:https://github.com/langchain-ai/langsmith-sdk.git
#!RemoteAsset:  sha256:9d00e54f54d833c1914003527ff03ad0364741034330da72f0adbeaba852b6cf
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# Skip optional Strands integration: No module named 'strands_agents'.
BuildOption(check):  -e 'langsmith.integrations.strands_agents*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(orjson)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-toolbelt)
BuildRequires:  python3dist(uuid-utils)
BuildRequires:  python3dist(websockets)
BuildRequires:  python3dist(xxhash)
BuildRequires:  python3dist(zstandard)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
LangSmith is a client library for tracing, monitoring, and evaluating LLM
applications through the LangSmith platform.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
