# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname debugpy

Name:           python-%{srcname}
Version:        1.8.21
Release:        %autorelease
Summary:        Debug Adapter Protocol implementation for Python
License:        MIT
URL:            https://github.com/microsoft/debugpy
#!RemoteAsset:  sha256:a3c53278e84c94e11bd87c53970ec391d1a67396c8b22609fcac576520e611a6
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l debugpy
# Windows-only module: ctypes has no attribute 'windll' on Linux.
BuildOption(check):  -e debugpy.launcher.winapi

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Debugpy is an implementation of the Debug Adapter Protocol for Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/debugpy
%{_bindir}/debugpy-adapter

%changelog
%autochangelog
