# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname apache-tvm-ffi
%global pypi_name apache_tvm_ffi

Name:           python-%{srcname}
Version:        0.1.11
Release:        %autorelease
Summary:        Open ABI and FFI for machine learning systems
License:        Apache-2.0
URL:            https://tvm.apache.org/ffi/
VCS:            git:https://github.com/apache/tvm-ffi.git
#!RemoteAsset:  sha256:153cd2c5a9717804cb0bcd9b2709f22a1e5f80ed05b5a490faf5949b136eedba
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  tvm_ffi
# An optional helper which imports PyTorch
BuildOption(check):  -e tvm_ffi.utils._build_optional_torch_c_dlpack
# Native shared libraries
BuildOption(check):  -e tvm_ffi.lib.libtvm_ffi
BuildOption(check):  -e tvm_ffi.lib.libtvm_ffi_testing

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(scikit-build-core) >= 0.10
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Apache TVM FFI provides an open ABI and foreign-function interface for machine
learning systems, including Python and C++ bindings used by XGrammar.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE NOTICE licenses/*
%{_bindir}/tvm-ffi-config
%{_bindir}/tvm-ffi-stubgen

%changelog
%autochangelog
