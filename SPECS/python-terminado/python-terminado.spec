# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname terminado

Name:           python-%{srcname}
Version:        0.18.1
Release:        %autorelease
Summary:        Tornado websocket backend for terminals
License:        BSD-2-Clause
URL:            https://github.com/jupyter/terminado
#!RemoteAsset:  sha256:de09f2c4b85de4765f7714688fff57d3e75bad1f909b589fde880460c753fd2e
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l terminado

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(ptyprocess)
BuildRequires:  python3dist(tornado)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Terminado provides a Tornado websocket backend for browser-based terminal
emulators.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
