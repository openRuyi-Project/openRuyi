# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langgraph

Name:           python-%{srcname}
Version:        1.2.4
Release:        %autorelease
Summary:        Stateful graph framework for building agents
License:        MIT
URL:            https://github.com/langchain-ai/langgraph
VCS:            git:https://github.com/langchain-ai/langgraph.git
#!RemoteAsset:  sha256:5df076973a2d23efb13eceb279d1e5b46feebcbbeded0a86a2ef669abd9e4399
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(langchain-core)
BuildRequires:  python3dist(langgraph-checkpoint)
BuildRequires:  python3dist(langgraph-prebuilt)
BuildRequires:  python3dist(langgraph-sdk)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(xxhash)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
LangGraph is a framework for building long-running, stateful agent workflows.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
