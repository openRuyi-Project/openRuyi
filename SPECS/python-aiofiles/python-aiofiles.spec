# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiofiles

Name:           python-%{srcname}
Version:        25.1.0
Release:        %autorelease
Summary:        File support for asyncio
License:        Apache-2.0
URL:            https://github.com/Tinche/aiofiles
#!RemoteAsset:  sha256:a8d728f0a29de45dc521f18f07297428d56992a742f0cd2701ba86e44d23d5b2
Source:         https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatch-vcs)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
aiofiles is an Apache2 licensed library, written in Python, for handling
local disk files in asyncio applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
