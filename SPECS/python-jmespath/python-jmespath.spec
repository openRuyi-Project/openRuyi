# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jmespath
%global pkgname jmespath

Name:           python-%{srcname}
Version:        1.0.1
Release:        %autorelease
Summary:        JSON Matching Expressions
License:        MIT
URL:            https://github.com/jmespath/jmespath.py
#!RemoteAsset:  sha256:90261b206d6defd58fdd5e85f478bf633a2901798906be2ad389150c5c60edbe
Source0:        https://files.pythonhosted.org/packages/source/j/jmespath/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install):  -l %{pkgname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
JMESPath (pronounced "james path") allows you to declaratively specify how to
extract elements from a JSON document.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{pkgname}-%{version}

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
