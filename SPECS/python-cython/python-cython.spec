# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname Cython

Name:           python-cython
Version:        3.2.4
Release:        %autorelease
Summary:        Language for writing Python extension modules
License:        Apache-2.0
URL:            http://www.cython.org
#!RemoteAsset:  sha256:9631e586c49b9d3f72c3962c376119479a6a98e3c0e3c14d5218e199ef563b18
Source:         https://github.com/cython/cython/archive/%{version}/Cython-%{version}.tar.gz#/cython-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  Cython cython pyximport
BuildOption(check):  -e 'Cython.Build.IpythonMagic'
BuildOption(check):  -e 'Cython.Build.Tests.TestIpythonMagic'
BuildOption(check):  -e 'Cython.Coverage'
BuildOption(check):  -e 'Cython.Debugger.Tests.TestLibCython'
BuildOption(check):  -e 'Cython.Debugger.Tests.test_libcython_in_gdb'
BuildOption(check):  -e 'Cython.Debugger.Tests.test_libpython_in_gdb'
BuildOption(check):  -e 'Cython.Debugger.libcython'
BuildOption(check):  -e 'Cython.Debugger.libpython'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       Cython = %{version}-%{release}
Provides:       Cython%{?_isa} = %{version}-%{release}
Provides:       cython = %{version}-%{release}
Provides:       cython%{?_isa} = %{version}-%{release}

Provides:       python3-cython = %{version}-%{release}
Provides:       python3-cython%{?_isa} = %{version}-%{release}
%python_provide python3-cython

%description
The Cython language makes writing C extensions for the Python language as easy
as Python itself. Cython is a source code translator based on Pyrex,
but supports more cutting edge functionality and optimizations.

The Cython language is a superset of the Python language (almost all Python
code is also valid Cython code), but Cython additionally supports optional
static typing to natively call C functions, operate with C++ classes and
declare fast C types on variables and class attributes.
This allows the compiler to generate very efficient C code from Cython code.

This makes Cython the ideal language for writing glue code for external C/C++
libraries, and for fast C modules that speed up the execution of Python code.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGES.rst USAGE.txt Demos Doc Tools
%{_bindir}/cython
%{_bindir}/cygdb
%{_bindir}/cythonize

%changelog
%autochangelog
