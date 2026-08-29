# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname kenlm

Name:           python-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        KenLM: Faster and Smaller Language Model Queries
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/kpu/kenlm
#!RemoteAsset:  sha256:c4628bb9fb63c8a6f9240035b8b037385cfc404cb72e933cf48878291edac1e8
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Drop the dependency python3dist(cmake) we do not have which is also unused
Patch2000:      2000-drop-cmake-dep.patch

BuildOption(install):  -l %{srcname} -L

BuildRequires:  cmake
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
KenLM is a library for estimating, filtering, and querying
language models with significantly lower memory usage.

%generate_buildrequires
%pyproject_buildrequires

%build -p
cython -3 --cplus python/kenlm.pyx -o python/kenlm.cpp

%files -f %{pyproject_files}
%license LICENSE COPYING COPYING.3 COPYING.LESSER.3
%{python3_sitearch}/libkenlm.so

%changelog
%autochangelog
