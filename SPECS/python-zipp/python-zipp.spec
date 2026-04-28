# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zipp

Name:           python-%{srcname}
Version:        3.23.0
Release:        %autorelease
Summary:        Backport of pathlib-compatible object wrapper for zip files
License:        MIT
URL:            https://github.com/jaraco/zipp
#!RemoteAsset:  sha256:a07157588a12518c9d4034df3fbbee09c814741a33ff63c05fa29d26a2404166
Source:         https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(coherent-licensed)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
