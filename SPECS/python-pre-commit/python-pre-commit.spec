# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pre-commit
%global pypiname pre_commit

Name:           python-%{srcname}
Version:        4.6.0
Release:        %autorelease
Summary:        Framework for managing and maintaining multi-language pre-commit hooks
License:        MIT
URL:            https://pre-commit.com
#!RemoteAsset:  sha256:718d2208cef53fdc38206e40524a6d4d9576d103eb16f0fec11c875e7716e9d9
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypiname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pre_commit
# Any Python files inside pre_commit.resources are templates and are not
# intended to be imported.
BuildOption(check):  -e 'pre_commit.resources.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cfgv)
BuildRequires:  python3dist(identify)
BuildRequires:  python3dist(nodeenv)
BuildRequires:  git-core

Requires:       git-core

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A framework for managing and maintaining multi-language pre-commit hooks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{srcname}

%changelog
%autochangelog
