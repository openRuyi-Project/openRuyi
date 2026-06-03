# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langchain-core
%global pypi_name langchain_core

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Core abstractions for building LangChain applications
License:        MIT
URL:            https://github.com/langchain-ai/langchain
VCS:            git:https://github.com/langchain-ai/langchain.git
#!RemoteAsset:  sha256:1dc341eed802ed9c117c0df3923c991e5e9e226571e5725c194eeb5bd93d1a7f
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jsonpatch)
BuildRequires:  python3dist(langchain-protocol)
BuildRequires:  python3dist(langsmith)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(tenacity)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(uuid-utils)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
langchain-core contains the base abstractions and runtime interfaces used by
the LangChain Python ecosystem.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
