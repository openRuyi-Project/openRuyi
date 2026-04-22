# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname multiprocess

Name:           python-%{srcname}
Version:        0.70.19
Release:        %autorelease
Summary:        Better multiprocessing and multithreading in Python
License:        BSD-3-Clause
URL:            https://github.com/uqfoundation/multiprocess
VCS:            git:https://github.com/uqfoundation/multiprocess
#!RemoteAsset:  sha256:952021e0e6c55a4a9fe4cd787895b86e239a40e76802a789d6305398d3975897
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} _multiprocess
BuildOption(check):  -e 'multiprocess.tests*' -e multiprocess.popen_spawn_win32

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(dill) >= 0.4.1

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
multiprocess is a fork of Python's multiprocessing package.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
