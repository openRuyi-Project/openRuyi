# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname numba

Name:           python-%{srcname}
Version:        0.66.0
Release:        %autorelease
Summary:        NumPy-aware dynamic Python compiler using LLVM
License:        BSD-2-Clause
URL:            https://numba.pydata.org/
VCS:            git:https://github.com/numba/numba.git
#!RemoteAsset:  sha256:b900e63a0e26c05ea9a6d5a3a5a0a177cb64c5011887bf43edb8c3ed2c38d363
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l numba
# missing CUDA
BuildOption(check):  -e 'numba.cuda.tests*'
# No module named '_gdb'
BuildOption(check):  -e 'numba.misc.gdb_print_extension'
# No module named 'source_module'
BuildOption(check):  -e 'numba.tests.pycc_distutils_usecase.setup_distutils'
BuildOption(check):  -e 'numba.tests.pycc_distutils_usecase.setup_setuptools'
# No module named 'nested'
BuildOption(check):  -e 'numba.tests.pycc_distutils_usecase.setup_distutils_nested'
BuildOption(check):  -e 'numba.tests.pycc_distutils_usecase.setup_setuptools_nested'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(llvmlite)
BuildRequires:  python3dist(nbformat)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Numba is an open source JIT compiler that translates a subset of Python and
NumPy code into fast machine code using LLVM.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGE_LOG
%doc README.rst
%license LICENSE
%license LICENSES.third-party
%exclude %{python3_sitearch}/%{srcname}/tests/__pycache__/cfunc_cache_usecases.*.nbc
%exclude %{python3_sitearch}/%{srcname}/tests/__pycache__/cfunc_cache_usecases.*.nbi
%{_bindir}/numba

%changelog
%autochangelog
