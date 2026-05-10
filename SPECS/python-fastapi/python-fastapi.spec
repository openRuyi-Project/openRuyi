# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fastapi

Name:           python-%{srcname}
Version:        0.136.1
Release:        %autorelease
Summary:        High-performance async web framework for building APIs
License:        MIT
URL:            https://github.com/fastapi/fastapi
VCS:            git:https://github.com/fastapi/fastapi.git
#!RemoteAsset:  sha256:7af665ad7acfa0a3baf8983d393b6b471b9da10ede59c60045f49fbc89a0fa7f
Source:         https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pdm-backend)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(httpx)

Requires:       python3dist(starlette)
Requires:       python3dist(pydantic)
Requires:       python3dist(typing-extensions)
Requires:       python3dist(typing-inspection)
Requires:       python3dist(annotated-doc)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
FastAPI is a modern, high-performance web framework for building APIs with
Python based on standard type hints. It is built on top of Starlette for web
routing and Pydantic for data validation.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/fastapi

%changelog
%autochangelog
