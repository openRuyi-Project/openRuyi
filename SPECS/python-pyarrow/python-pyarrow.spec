# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyarrow

Name:           python-%{srcname}
Version:        23.0.1
Release:        %autorelease
Summary:        Python bindings for Apache Arrow
License:        Apache-2.0
URL:            https://arrow.apache.org/
VCS:            git:https://github.com/apache/arrow
#!RemoteAsset:  sha256:b8c5873e33440b2bc2f4a79d2b47017a89c5a24116c055625e6f2ee50523f019
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
# No cuda
BuildOption(check):  -e pyarrow.cuda
BuildOption(check):  -e pyarrow.tests.test_cuda
BuildOption(check):  -e pyarrow.tests.test_cuda_numba_interop
# The pyarrow installation is not built with support for 'flight'
BuildOption(check):  -e pyarrow.flight
BuildOption(check):  -e pyarrow.tests.test_flight_async
# No module named 'pyarrow._orc'
BuildOption(check):  -e pyarrow.libarrow_python
BuildOption(check):  -e pyarrow.orc
# No module named 'pyarrow._parquet_encryption'
BuildOption(check):  -e pyarrow.parquet.encryption
# The pyarrow installation is not built with support for 'substrait'
BuildOption(check):  -e pyarrow.substrait
# The pyarrow installation is not built with support for 'flight'
BuildOption(check):  -e pyarrow.tests.arrow_16597
# No module named 'pyarrow._parquet_encryption'
BuildOption(check):  -e pyarrow.tests.parquet.encryption
# Test error?
BuildOption(check):  -e pyarrow.tests.read_record_batch
# No module named 'jpype'
BuildOption(check):  -e pyarrow.tests.test_jvm

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  arrow-devel
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(numpy) >= 1.25
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm[toml])
# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(hypothesis)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyArrow is the Python interface for Apache Arrow, providing zero-copy data
interchange with Arrow arrays and tables together with Arrow-backed file and
IPC formats.

%generate_buildrequires
%pyproject_buildrequires

%build -p
export PYARROW_BUNDLE_ARROW_CPP=0
export PYARROW_WITH_FLIGHT=0
export PYARROW_WITH_GANDIVA=0
export PYARROW_WITH_SUBSTRAIT=0
export PYARROW_WITH_ORC=0
export PYARROW_WITH_S3=0
export PYARROW_WITH_GCS=0
export PYARROW_WITH_AZURE=0
export PYARROW_WITH_HDFS=0
%ifarch riscv64
# Work around RVV-related compiler ICE in vendored xxhash header.
export PYARROW_CXXFLAGS="-DXXH_VECTOR=0"
%endif

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt NOTICE.txt

%changelog
%autochangelog
