# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httptools

Name:           python-%{srcname}
Version:        0.7.1
Release:        %autorelease
Summary:        A collection of framework independent HTTP protocol utils
License:        MIT
URL:            https://github.com/MagicStack/httptools
VCS:            git:https://github.com/MagicStack/httptools.git
#!RemoteAsset:  sha256:abd72556974f8e7c74a259655924a717a2365b236c882c3f6f8a45fe94703ac9
Source:         https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A collection of framework independent HTTP protocol utils. httptools is a
Python binding for the nodejs HTTP parser, providing high-performance HTTP
parsing capabilities.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
