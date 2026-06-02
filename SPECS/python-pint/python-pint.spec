# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pint

Name:           python-%{srcname}
Version:        0.25.2
Release:        %autorelease
Summary:        Physical quantities module
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/pint
#!RemoteAsset:  sha256:85a45d1da8fe9c9f7477fed8aef59ad2b939af3d6611507e1a9cbdacdcd3450a
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# skip tests: missing python-matplotlib
BuildOption(check):  -e 'pint.matplotlib'
BuildOption(check):  -e 'pint.testsuite.test_matplotlib'
# skip tests: No module named 'sparse'
BuildOption(check):  -e 'pint.testsuite.test_compat_downcast'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(dask)
BuildRequires:  python3dist(distributed)
BuildRequires:  python3dist(flexcache)
BuildRequires:  python3dist(flexparser)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(platformdirs)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(xarray)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pint is a Python package to define, operate and manipulate physical quantities
with units.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/pint-convert

%changelog
%autochangelog
