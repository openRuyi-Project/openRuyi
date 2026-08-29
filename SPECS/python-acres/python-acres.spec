# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname acres

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Access resources on your terms
License:        Apache-2.0
URL:            https://github.com/nipreps/acres
#!RemoteAsset:  sha256:128b6447bf5df3b6210264feccbfa018b4ac5bd337358319aec6563f99db8f3a
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pdm-backend)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This module aims to provide a simple way to access package resources
that will fit most use cases.

%generate_buildrequires -p
export PDM_BUILD_SCM_VERSION='%{version}'

%build -p
export PDM_BUILD_SCM_VERSION='%{version}'

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
