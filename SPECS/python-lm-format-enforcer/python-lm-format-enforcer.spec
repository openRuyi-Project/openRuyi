# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname lm-format-enforcer
%global pypi_name lm_format_enforcer

Name:           python-%{srcname}
Version:        0.11.3
Release:        %autorelease
Summary:        Enforce the output format (JSON Schema, Regex etc) of a language model
License:        MIT
URL:            https://github.com/noamgat/lm-format-enforcer
#!RemoteAsset:  sha256:e68081c108719cce284a9bcc889709b26ffb085a1945b5eba3a12cfa96d528da
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l lmformatenforcer -L
BuildOption(check):  -e lmformatenforcer.integrations.*

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(interegular)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(numpy)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Enforce the output format (JSON Schema, Regex etc) of a language model.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
