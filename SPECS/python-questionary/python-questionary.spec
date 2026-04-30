# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname questionary

Name:           python-%{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        Python library to build pretty command line prompts
License:        MIT
URL:            https://github.com/tmbo/questionary
#!RemoteAsset:  sha256:3d7e980292bb0107abaa79c68dd3eee3c561b83a0f89ae482860b181c8bd412d
Source0:        https://files.pythonhosted.org/packages/source/q/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Questionary is a Python library for building interactive command line prompts.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md NOTICE
%license LICENSE

%changelog
%autochangelog
