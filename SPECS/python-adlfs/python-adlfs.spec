# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname adlfs

Name:           python-%{srcname}
Version:        2026.8.0
Release:        %autorelease
Summary:        Fsspec interface for Azure Data Lake Storage
License:        BSD-3-Clause
URL:            https://github.com/fsspec/adlfs
#!RemoteAsset:  sha256:b78a01bd892c2a99f461b2b2ef4592c2eb45934e728f318472291ccaa6378e06
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
BuildOption(check):    -e %{srcname}.tests -e '%{srcname}.tests.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(azure-core) >= 1.28
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-storage-blob) >= 12.17
BuildRequires:  python3dist(fsspec) >= 2023.12
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm) >= 7

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Adlfs provides fsspec-compatible filesystems for Azure Blob Storage and
Azure Data Lake Storage Gen2.

%generate_buildrequires
%pyproject_buildrequires

%install -a
# The upstream wheel includes its test suite in the runtime package.
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/tests
sed -i '\#/%{srcname}/tests#d' %{pyproject_files}

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE.txt

%changelog
%autochangelog
