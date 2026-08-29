# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname xyzservices

Name:           python-%{srcname}
Version:        2026.3.0
Release:        %autorelease
Summary:        Source of XYZ tiles providers
License:        BSD-3-Clause
URL:            https://github.com/geopandas/xyzservices
#!RemoteAsset:  sha256:d226866a5d8e9fef337034d8da37a8298f0a1d9d1489b4018e69579eb321fea4
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(mercantile)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
xyzservices is a library that provides a unified API for XYZ tile providers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_datadir}/xyzservices/providers.json

%changelog
%autochangelog
