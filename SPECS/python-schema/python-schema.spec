# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname schema

Name:           python-%{srcname}
Version:        0.7.8
Release:        %autorelease
Summary:        Schema validation just got Pythonic
License:        MIT
URL:            https://github.com/keleshev/schema
#!RemoteAsset:  sha256:e86cc08edd6fe6e2522648f4e47e3a31920a76e82cce8937535422e310862ab5
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
schema is a library for validating Python data structures,
such as those obtained from config-files, forms, external services or
command-line parsing, converted from JSON/YAML (or something else) to Python data-types.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE-MIT

%changelog
%autochangelog
