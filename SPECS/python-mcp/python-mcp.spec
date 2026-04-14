# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mcp

Name:           python-mcp
Version:        1.26.0
Release:        %autorelease
Summary:        Model Context Protocol SDK
License:        MIT
URL:            https://github.com/modelcontextprotocol/python-sdk
#!RemoteAsset:  sha256:db6e2ef491eecc1a0d93711a76f28dec2e05999f93afd48795da1c1137142c66
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz

# Patches
# Disable uv-dynamic-versioning to keep the build fully source-tarball based
Patch2000:      2000-python-mcp-drop-uv-dynamic-versioning.patch
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(check):  mcp
BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(httpx-sse)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pydantic-settings)
BuildRequires:  python3dist(pyjwt)
BuildRequires:  python3dist(python-multipart)
BuildRequires:  python3dist(sse-starlette)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(typing-inspection)
BuildRequires:  python3dist(uvicorn)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python SDK for the Model Context Protocol (MCP), providing client and server
components for MCP-based integrations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
