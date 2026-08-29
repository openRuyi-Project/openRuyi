# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname contourpy

Name:           python-%{srcname}
Version:        1.3.3
Release:        %autorelease
Summary:        Python library for calculating contours in 2D quadrilateral grids
License:        BSD-3-Clause
URL:            https://contourpy.readthedocs.io/
#!RemoteAsset:  sha256:083e12155b210502d0bca491432bb04d56dc3432f95a979b429f2848c3dbe880
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# Bokeh is optional.
# TODO: Add python-bokeh.
BuildOption(check):  -e contourpy.util.bokeh_renderer
# Circular dependency.
BuildOption(check):  -e contourpy.util.mpl_renderer
BuildOption(check):  -e contourpy.util.mpl_util

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  gcc-c++

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ContourPy is a Python library for calculating contours of 2D quadrilateral
grids. It is written in C++11 and wrapped using pybind11.

It contains the 2005 and 2014 algorithms used in Matplotlib as well as a newer
algorithm that includes more features and is available in both serial and
multithreaded versions. It provides an easy way for Python libraries to use
contouring algorithms without having to include Matplotlib as a dependency.

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
