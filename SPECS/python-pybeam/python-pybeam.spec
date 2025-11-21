# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pybeam

Name:           python-%{srcname}
Version:        0.8.1
Release:        %autorelease
Summary:        Python module to parse Erlang BEAM files
License:        MIT
URL:            https://github.com/matwey/pybeam
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install): -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Python module to parse Erlang BEAM files, now it is able to read
imports, exports, atoms, as well as compile info and attribute
chunks in pretty python format.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%{?autochangelog}
