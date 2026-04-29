# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cattrs

Name:           python-%{srcname}
Version:        26.1.0
Release:        %autorelease
Summary:        Composable class support for attrs and dataclasses
License:        MIT
URL:            https://github.com/python-attrs/cattrs
VCS:            git:https://github.com/python-attrs/cattrs
#!RemoteAsset:  sha256:fa239e0f0ec0715ba34852ce813986dfed1e12117e209b816ab87401271cdd40
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} cattr +auto
BuildOption(check):  -e "cattrs.preconf.*"
BuildOption(check):  -e "cattr.preconf.*"

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(attrs) >= 25.4
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions) >= 4.14
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cattrs provides composable support for attrs and dataclasses classes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE*

%changelog
%autochangelog
