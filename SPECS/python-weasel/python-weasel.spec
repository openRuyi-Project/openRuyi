# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname weasel

Name:           python-%{srcname}
Version:        0.4.3
Release:        %autorelease
Summary:        A small and easy workflow system
License:        MIT
URL:            https://github.com/explosion/weasel
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cloudpathlib)
BuildRequires:  python3dist(confection)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(smart-open)
BuildRequires:  python3dist(srsly)
BuildRequires:  python3dist(typer-slim)
BuildRequires:  python3dist(wasabi)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Weasel lets you manage and share end-to-end workflows for different use
cases and domains, and orchestrate training, packaging and serving your
custom pipelines.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/weasel

%changelog
%autochangelog
