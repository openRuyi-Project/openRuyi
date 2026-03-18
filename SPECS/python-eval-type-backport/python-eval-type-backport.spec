# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname eval-type-backport

Name:           python-%{srcname}
Version:        0.3.1
Release:        %autorelease
Summary:        Like typing._eval_type, but lets older Python versions use newer typing features
License:        MIT
URL:            https://github.com/alexmojaki/eval_type_backport
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/eval_type_backport-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  eval_type_backport

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
eval_type_backport is a backport of typing._eval_type that allows older Python
versions to use newer typing features such as X | Y union syntax and
from __future__ import annotations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt

%changelog
%{?autochangelog}
