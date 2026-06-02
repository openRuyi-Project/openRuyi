# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname heapdict
%global pypi_name HeapDict

Name:           python-%{srcname}
Version:        1.0.1
Release:        %autorelease
Summary:        A heap with decrease-key and increase-key operations
License:        BSD-3-Clause
URL:            https://github.com/DanielStutzbach/heapdict
#!RemoteAsset:  sha256:8495f57b3e03d8e46d5f1b2cc62ca881aca392fd5cc048dc0aa2e1a6d23ecdb6
Source0:        https://files.pythonhosted.org/packages/source/H/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
HeapDict is a heap with decrease-key and increase-key operations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
