# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname unidic-lite

Name:           python-%{srcname}
Version:        1.0.8
Release:        %autorelease
Summary:        Small UniDic dictionary package for Python
License:        MIT AND BSD-3-Clause
URL:            https://github.com/polm/unidic-lite
#!RemoteAsset:  sha256:db9d4572d9fdd4d00a97949d4b0741ec480ee05a7e7e2e32f547500dae27b245
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l unidic_lite
BuildOption(check):  unidic_lite

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
unidic-lite provides a compact UniDic dictionary packaged for Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md unidic_lite/dicdir/README.md
%license LICENSE LICENSE.unidic

%changelog
%autochangelog
