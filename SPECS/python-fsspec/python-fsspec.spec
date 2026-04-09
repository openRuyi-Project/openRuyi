# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fsspec

Name:           python-%{srcname}
Version:        2026.2.0
Release:        %autorelease
Summary:        File-system specification for Python
License:        BSD-3-Clause
URL:            https://pypi.org/project/fsspec/
VCS:            git:https://github.com/fsspec/filesystem_spec
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
BuildOption(check):  -e 'fsspec.tests.*' -e 'fsspec.implementations.*' -e fsspec.conftest -e fsspec.fuse -e fsspec.gui

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Fsspec provides a unified Python interface for local, remote, and embedded
filesystems.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
