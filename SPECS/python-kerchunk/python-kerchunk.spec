# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname kerchunk

Name:           python-%{srcname}
Version:        0.2.10
Release:        %autorelease
Summary:        Functions to create references for chunked data
License:        MIT
URL:            https://fsspec.github.io/kerchunk/
VCS:            git:https://github.com/fsspec/kerchunk.git
#!RemoteAsset:  sha256:aae63c0fe4ca2e97025f026578a0577545011fe6679751392c815e0d1d6bf954
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l kerchunk
# Skip tests: No module named 'tifffile' (circular dependency)
BuildOption(check):  -e 'kerchunk.tiff'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(astropy)
BuildRequires:  python3dist(cfgrib)
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(numcodecs)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(ujson)
BuildRequires:  python3dist(xarray)
BuildRequires:  python3dist(zarr)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Kerchunk creates references that expose archival and scientific data through
fsspec-compatible virtual Zarr stores without copying the original data.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
