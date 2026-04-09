# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname wrapt

Name:           python-%{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        A Python module for decorators, wrappers and monkey patching
License:        BSD-2-Clause
URL:            https://github.com/GrahamDumpleton/wrapt
#!RemoteAsset:  sha256:5fdcb09bf6db023d88f312bd0767594b414655d58090fc1c46b3414415f67fac
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The aim of the **wrapt** module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

The **wrapt** module focuses very much on correctness. It therefore goes
way beyond existing mechanisms such as ``functools.wraps()`` to ensure that
decorators preserve introspectability, signatures, type checking abilities
etc. The decorators that can be constructed using this module will work in
far more scenarios than typical decorators and provide more predictable and
consistent behaviour.

To ensure that the overhead is as minimal as possible, a C extension module
is used for performance critical components. An automatic fallback to a
pure Python implementation is also provided where a target system does not
have a compiler to allow the C extension to be compiled.

Documentation
-------------

For further information on the **wrapt** module see:

* http://wrapt.readthedocs.org/

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
