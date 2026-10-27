# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httptools

Name:           python-%{srcname}
Version:        0.9.0
Release:        %autorelease
Summary:        A collection of framework independent HTTP protocol utils
License:        MIT
URL:            https://github.com/MagicStack/httptools
VCS:            git:https://github.com/MagicStack/httptools.git
#!RemoteAsset:  sha256:d484ebb7e3a3f3597b0f645fbd1b85633674ca808c1f5ba11c2caf7c66f5c8b6
Source:         https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A collection of framework independent HTTP protocol utils. httptools is a
Python binding for the nodejs HTTP parser, providing high-performance HTTP
parsing capabilities.

%prep -a
# Relax exact version pins on setuptools.
sed -i 's/"setuptools>=80\.9\.0,<=82\.0\.1"/"setuptools>=80.9.0"/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
