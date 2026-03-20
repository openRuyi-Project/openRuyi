# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tenacity

Name:           python-%{srcname}
Version:        9.1.4
Release:        %autorelease
Summary:        General-purpose retrying library for Python
License:        Apache-2.0
URL:            https://github.com/jd/tenacity
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  tenacity
# tenacity.tornadoweb requires tornado which is not packaged
BuildOption(check):  -e 'tenacity.tornadoweb*'

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Tenacity is a general-purpose retrying library to simplify the task of adding
retry behavior to just about anything. It is a fork of retrying that supports
async, context managers, and more.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
