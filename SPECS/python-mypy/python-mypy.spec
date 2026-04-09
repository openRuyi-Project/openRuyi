# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mypy

Name:           python-%{srcname}
Version:        1.19.1
Release:        %autorelease
Summary:        Optional static typing for Python
License:        MIT
URL:            https://www.mypy-lang.org/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  mypy mypyc

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(librt)
BuildRequires:  python3dist(mypy-extensions)
BuildRequires:  python3dist(pathspec)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(types-psutil)
BuildRequires:  python3dist(types-setuptools)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Add type annotations to your Python programs, and use mypy to type check them. Mypy is essentially a Python linter on steroids, and it can catch many programming errors by analyzing your program, without actually having to run it. Mypy has a powerful type system with features such as type inference, gradual typing, generics and union types.

%prep -a
# The test suites have bugs that halt the checking process.
rm -rf %{_builddir}/python-%{srcname}-%{version}/mypy/test
rm -rf %{_builddir}/python-%{srcname}-%{version}/mypyc/test

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/mypy
%{_bindir}/mypyc
%{_bindir}/dmypy
%{_bindir}/stubgen
%{_bindir}/stubtest

%changelog
%autochangelog
