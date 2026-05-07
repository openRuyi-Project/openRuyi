# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname invoke

Name:           python-%{srcname}
Version:        3.0.3
Release:        %autorelease
Summary:        Pythonic task execution
License:        BSD-3-Clause
URL:            https://www.pyinvoke.org/
#!RemoteAsset:  sha256:437b6a622223824380bfb4e64f612711a6b648c795f565efc8625af66fb57f0c
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
# No modules named 'yaml'
BuildOption(check):  -e invoke.vendor.yaml.cyaml

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Invoke is a Python task execution tool and library, drawing inspiration
from various sources to arrive at a powerful and clean feature set.  It is
evolved from the Fabric project, but focuses on local and abstract concerns
instead of servers and network commands.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
