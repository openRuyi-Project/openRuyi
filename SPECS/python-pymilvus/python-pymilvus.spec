# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pymilvus

Name:           python-%{srcname}
Version:        2.6.9
Release:        %autorelease
Summary:        Python Sdk for Milvus
License:        Apache-2.0
URL:            https://github.com/milvus-io/pymilvus
#!RemoteAsset:  sha256:c53a3d84ff15814e251be13edda70a98a1c8a6090d7597a908387cbb94a9504a
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Skip bulk_writer, don't need it for now
BuildOption(check):  -e "pymilvus.bulk_writer" -e "pymilvus.bulk_writer.*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python SDK for Milvus.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
