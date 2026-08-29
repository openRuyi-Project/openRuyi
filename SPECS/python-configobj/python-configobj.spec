# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname configobj

Name:           python-%{srcname}
Version:        5.0.9
Release:        %autorelease
Summary:        Config file reading, writing, and validation
License:        BSD-3-Clause
URL:            https://github.com/DiffSK/configobj
#!RemoteAsset:  sha256:03c881bbf23aa07bccf1b837005975993c4ab4427ba57f959afdd9d1a2386848
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} validate

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ConfigObj is a simple but powerful configuration file reader and writer: an ini
file round tripper. Its main feature is that it is very easy to use, with a
straightforward programmers interface and a simple syntax for config files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
