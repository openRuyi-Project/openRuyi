# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pymilvus

Name:           python-%{srcname}
Version:        2.6.16
Release:        %autorelease
Summary:        Python Sdk for Milvus
License:        Apache-2.0
URL:            https://github.com/milvus-io/pymilvus
#!RemoteAsset:  sha256:0ad2518252224ec4ec663b1d17a89bb9c404d089c15e70888aabd021cd258ccf
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Our hatchling maybe newer than upstream
Patch2000:      2000-Relax-hatchling-version.patch

BuildOption(install):  -l %{srcname}
# Skip bulk_writer, don't need it for now
BuildOption(check):  -e "pymilvus.bulk_writer" -e "pymilvus.bulk_writer.*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(gitpython)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python SDK for Milvus.

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_PYMILVUS=%{version}
%pyproject_buildrequires

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_PYMILVUS=%{version}

%install -p
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_PYMILVUS=%{version}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
