# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname llvmlite

Name:           python-%{srcname}
Version:        0.48.0
Release:        %autorelease
Summary:        Lightweight LLVM Python binding for writing JIT compilers
License:        BSD-2-Clause AND Apache-2.0 WITH LLVM-exception
URL:            https://github.com/numba/llvmlite
#!RemoteAsset:  sha256:543b19f9ef8f3c7c60d1468191e4ee1b1537bf9f8a3d56f64c0ddd98de92edd2
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l llvmlite
# libllvmlite.so is a ctypes-loaded shared library, not a CPython extension
BuildOption(check):  -e llvmlite.binding.libllvmlite

BuildRequires:  cmake
BuildRequires:  llvm-devel
BuildRequires:  llvm-static
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
llvmlite is a lightweight LLVM Python binding for writing JIT compilers. It
provides a Python API for generating LLVM IR and a C API wrapper around LLVM.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%ifarch riscv64
# vector.body missing on riscv64
# https://github.com/numba/llvmlite/issues/1449
%pytest -v llvmlite/tests \
    --deselect llvmlite/tests/test_binding.py::TestNewModulePassManager::test_optsize_minsize
%else
%pytest -v llvmlite/tests
%endif

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%license LICENSE.thirdparty

%changelog
%autochangelog
