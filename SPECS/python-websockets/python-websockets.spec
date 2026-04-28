# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname websockets

Name:           python-%{srcname}
Version:        16.0
Release:        %autorelease
Summary:        An implementation of the WebSocket Protocol (RFC 6455 and 7692)
License:        BSD-3-Clause
URL:            https://github.com/python-websockets/websockets
VCS:            git:https://github.com/python-websockets/websockets.git
#!RemoteAsset:  sha256:5f6261a5e56e8d5c42a4497b364ea24d94d9563e8fbd44e78ac40879c60179b5
Source:         https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An implementation of the WebSocket Protocol (RFC 6455 and 7692).
websockets is a library for building WebSocket servers and clients
in Python with a focus on correctness, simplicity, robustness, and
performance.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/websockets

%changelog
%autochangelog
