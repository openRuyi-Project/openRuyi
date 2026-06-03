# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langgraph-prebuilt
%global pypi_name langgraph_prebuilt

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Prebuilt components for LangGraph agents and tools
License:        MIT
URL:            https://github.com/langchain-ai/langgraph
VCS:            git:https://github.com/langchain-ai/langgraph.git
#!RemoteAsset:  sha256:3c579cf6eed2d17f9c157c2d0fcaddcd8688524e7022d3b22b37a3bf4589d528
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l langgraph
# Skip modules needing python-langgraph during bootstrap: No module named 'langgraph.stream'.
BuildOption(check):  -e 'langgraph.prebuilt*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(langchain-core)
BuildRequires:  python3dist(langgraph-checkpoint)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
langgraph-prebuilt provides high-level APIs for building LangGraph agents and tools.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
