# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname setuptools-git-ls-files
%global pypi_name setuptools_git_ls_files

Name:           python-%{srcname}
Version:        0.1.2
Release:        %autorelease
Summary:        Use git to list all files including submodules
License:        MIT
URL:            https://github.com/brainwane/setuptools-git-ls-files
VCS:            git:https://github.com/brainwane/setuptools-git-ls-files
#!RemoteAsset:  sha256:7d612087430dc912f0dca7a35c99bf791b2f86b7fa5a40c5a562192947c86efa
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l setuptools_git_ls_files +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
setuptools-git-ls-files provides a setuptools plugin that uses git ls-files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE*

%changelog
%autochangelog
