# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bleach

Name:           python-%{srcname}
Version:        6.4.0
Release:        %autorelease
Summary:        Safelist-based HTML sanitizing library
License:        Apache-2.0
URL:            https://github.com/mozilla/bleach
#!RemoteAsset:  sha256:4202482733d85cedd04e59fcb2f89f4e4c7c385a78d3c3c23c30446843a37452
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l bleach

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tinycss2)
BuildRequires:  python3dist(webencodings)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Bleach is a safelist-based HTML sanitizing library that removes potentially
unsafe markup from untrusted input.

%pyproject_extras_subpkg -n python-%{srcname} css

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
