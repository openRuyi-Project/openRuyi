# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tifffile

Name:           python-%{srcname}
Version:        2026.6.1
Release:        %autorelease
Summary:        Read and write TIFF files
License:        BSD-3-Clause
URL:            https://github.com/cgohlke/tifffile
#!RemoteAsset:  sha256:626c892c0e899d959b9438e7c0e1491dc154a7fead1f1f37a991724a50eceba9
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l tifffile

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(dask)
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(imagecodecs)
BuildRequires:  python3dist(kerchunk)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numcodecs)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(xarray)
BuildRequires:  python3dist(zarr)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Tifffile is a Python library for reading and writing TIFF image files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/lsm2bin
%{_bindir}/tiff2fsspec
%{_bindir}/tiffcomment
%{_bindir}/tifffile

%changelog
%autochangelog
