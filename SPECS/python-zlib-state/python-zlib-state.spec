# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zlib-state
%global pypi_name zlib_state

Name:           python-%{srcname}
Version:        0.1.12
Release:        %autorelease
Summary:        Save and restore zlib state
License:        MIT
URL:            https://github.com/seanmacavaney/zlib-state
#!RemoteAsset:  sha256:ccbb06321daf165b022aa4d22d62effb7df76f55035d50bbe8b93696db416cf0
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l zlib_state -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  pkgconfig(zlib)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
zlib-state provides helpers for saving and restoring zlib decompression state.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{python3_sitearch}/_zlib_state*.so

%changelog
%autochangelog
