# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rhoknp

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        Yet another Python binding for Juman++/KNP/KWJA
License:        MIT
URL:            https://github.com/ku-nlp/rhoknp
VCS:            git:https://github.com/ku-nlp/rhoknp.git
#!RemoteAsset:  sha256:083a0c75718a1b192dccbff1669267924b39af30c2445656b5e08adbd6b3be7f
Source:         https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(typer-slim)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(fastapi)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(uvicorn)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
rhoknp is a Python binding for Japanese NLP tools including Juman++, KNP,
and KWJA. It provides a unified interface for morphological analysis,
dependency parsing, and other Japanese language processing tasks.

%prep -a
# Replace uv_build backend with hatchling (compatible, uv_build not packaged)
sed -i 's/requires = \["uv_build"\]/requires = ["hatchling"]/' pyproject.toml
sed -i 's/build-backend = "uv_build"/build-backend = "hatchling.build"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/rhoknp

%changelog
%autochangelog
