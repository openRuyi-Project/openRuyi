# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cerberus

Name:           python-%{srcname}
Version:        1.3.8
Release:        %autorelease
Summary:        Schema and data validation for Python dictionaries
License:        ISC
URL:            https://github.com/pyeve/cerberus
VCS:            git:https://github.com/pyeve/cerberus.git
#!RemoteAsset:  sha256:579554887ffd189226774b87570f4a76db75cf0efcbaffcacd5e98b8ee877f61
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Cerberus validates and normalizes Python dictionaries against schemas.
It supports extending the available validation rules and data types.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
