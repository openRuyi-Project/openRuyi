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
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

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

Provides:       python3-%{srcname}
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

%check
# tests are skipped for now due missing test-only optional dependencies.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt NOTICE.txt

%changelog
%autochangelog
