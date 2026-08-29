# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname blis

Name:           python-%{srcname}
Version:        1.3.3
Release:        %autorelease
Summary:        The Blis BLAS-like linear algebra library, as a self-contained C-extension.
License:        BSD-3-Clause
URL:            https://github.com/explosion/cython-blis
#!RemoteAsset:  sha256:034d4560ff3cc43e8aa37e188451b0440e3261d989bb8a42ceee865607715ecd
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Upstream has not yet released a new version
# https://github.com/explosion/cython-blis/commit/1498af063ea924e2e2334a3f5ab49ae1a66a8648
Patch0:         0001-disable-obsolete-avx512-flags.patch

BuildOption(install):  -l %{srcname}
# Benchmark is no longer maintained
BuildOption(check):  -e "blis.benchmark"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(hypothesis)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This repository provides the Blis linear algebra routines as a self-contained Python C-extension.

%generate_buildrequires
%pyproject_buildrequires

%build -p
# cc1: error: bad value ‘knl’ for ‘-march=’ switch
# https://gcc.gnu.org/gcc-15/changes.html#x86
# RISC-V also needs it because the project does not provide support for it
export BLIS_ARCH="generic"

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
