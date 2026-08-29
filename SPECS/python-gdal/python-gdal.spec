# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gdal
%global pypi_name gdal

Name:           python-%{srcname}
Version:        3.13.1
Release:        %autorelease
Summary:        Python bindings for GDAL
License:        MIT
URL:            https://gdal.org/
VCS:            git:https://github.com/OSGeo/gdal.git
#!RemoteAsset:  sha256:94bb64d729ce73ceb75a314a15cba92696cdd854d99b6bf6b88a7b551227db74
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

# Use NumPy's supported FFT implementation
Patch2000:      2000-use-numpy-fft.patch

BuildOption(install):  osgeo osgeo_utils

BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Requires:       gdal%{?_isa} >= %{version}
Requires:       python3dist(fsspec)
Requires:       python3dist(h5py)
Requires:       python3dist(numpy)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python bindings and utilities for GDAL.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/gdal*
%{_bindir}/ogr*
%{_bindir}/pct2rgb*
%{_bindir}/rgb2pct*

%changelog
%autochangelog
