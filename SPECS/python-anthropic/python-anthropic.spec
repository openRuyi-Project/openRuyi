# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname anthropic

Name:           python-anthropic
Version:        0.86.0
Release:        %autorelease
Summary:        Official Python library for the Anthropic API
License:        MIT
URL:            https://github.com/anthropics/anthropic-sdk-python
#!RemoteAsset:  sha256:60023a7e879aa4fbb1fed99d487fe407b2ebf6569603e5047cfe304cebdaa0e5
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(check):  -e anthropic.lib.tools.mcp anthropic
BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(docstring-parser)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(jiter)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(sniffio)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
anthropic is the official Python SDK for accessing Anthropic APIs, with both
synchronous and asynchronous clients.

%prep
%autosetup -n anthropic-%{version}
# Align with available hatchling in distro while preserving minimum upstream requirement.
sed -i 's/hatchling==1.26.3/hatchling>=1.26.3/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog
