# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langgraph-sdk
%global pypi_name langgraph_sdk

Name:           python-%{srcname}
Version:        0.4.11
Release:        %autorelease
Summary:        SDK for interacting with LangGraph API
License:        MIT
URL:            https://github.com/langchain-ai/langgraph
VCS:            git:https://github.com/langchain-ai/langgraph.git
#!RemoteAsset:  sha256:2550af3bc7cb78ac4facb97d141ec1a76568fa3eb3d29040cff70b45bda84740
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(langchain-core)
BuildRequires:  python3dist(langchain-protocol)
BuildRequires:  python3dist(orjson)
BuildRequires:  python3dist(websockets)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
langgraph-sdk is an SDK for interacting with the LangGraph API.

%prep -a
# Relax for the websockets version packaged in openRuyi.
sed -i 's/"websockets>=14,<16"/"websockets>=14"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Integration tests require the separate langgraph-api server stack.
%pytest --ignore=tests/integration

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
