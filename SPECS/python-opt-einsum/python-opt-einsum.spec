# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opt-einsum
%global pypi_name opt_einsum

Name:           python-%{srcname}
Version:        3.4.0
Release:        %autorelease
Summary:        Path optimization of einsum functions
License:        MIT
URL:            https://github.com/dgasmith/opt_einsum
#!RemoteAsset:  sha256:96ca72f1b886d148241348783498194c577fa30a8faac108586b14f1ba4473ac
Source0:        https://files.pythonhosted.org/packages/source/o/opt-einsum/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Optimized einsum can significantly reduce the overall execution time
of einsum-like expressions (e.g., np.einsum, dask.array.einsum,
pytorch.einsum, tensorflow.einsum, ) by optimizing the expression's
contraction order and dispatching many operations to canonical BLAS,
cuBLAS, or other specialized routines.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
