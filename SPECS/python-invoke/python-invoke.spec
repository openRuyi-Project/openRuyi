# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname invoke

Name:           python-%{srcname}
Version:        2.2.1
Release:        %autorelease
License:        BSD-3-Clause
URL:            https://www.pyinvoke.org/
Summary:        Pythonic task execution
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install): -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel


Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Invoke is a Python task execution tool and library, drawing inspiration
from various sources to arrive at a powerful and clean feature set.  It is
evolved from the Fabric project, but focuses on local and abstract concerns
instead of servers and network commands.

%generate_buildrequires
%pyproject_buildrequires

# TODO: Enable tests.
%check


%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
