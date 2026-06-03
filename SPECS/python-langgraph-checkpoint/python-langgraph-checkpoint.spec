# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langgraph-checkpoint
%global pypi_name langgraph_checkpoint

Name:           python-%{srcname}
Version:        4.1.1
Release:        %autorelease
Summary:        Base interfaces for LangGraph checkpoint savers
License:        MIT
URL:            https://github.com/langchain-ai/langgraph
VCS:            git:https://github.com/langchain-ai/langgraph.git
#!RemoteAsset:  sha256:6c2bdb530c91f91d7d9c1bd100925d0fc4f498d418c17f3587d1526279482a25
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l langgraph

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(langchain-core)
BuildRequires:  python3dist(ormsgpack)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
langgraph-checkpoint defines the base interfaces for LangGraph checkpointers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
