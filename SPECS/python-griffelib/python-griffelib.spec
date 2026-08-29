# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname griffelib

Name:           python-%{srcname}
Version:        2.0.2
Release:        %autorelease
Summary:        Griffe core library for Python API signatures
License:        ISC
URL:            https://github.com/mkdocstrings/griffe
#!RemoteAsset:  sha256:3cf20b3bc470e83763ffbf236e0076b1211bac1bc67de13daf494640f2de707e
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  griffe

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pdm-backend)
BuildRequires:  python3dist(uv-dynamic-versioning)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Core library of Griffe, providing the ability to extract the structure, the
frame, the skeleton of Python projects, to generate API documentation or find
breaking changes in APIs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
