# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname azure-storage-blob
%global pypi_name azure_storage_blob
%global modname azure

Name:           python-%{srcname}
Version:        12.28.0
Release:        %autorelease
Summary:        Azure Storage Blobs client library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
#!RemoteAsset:  sha256:e7d98ea108258d29aa0efbfd591b2e2075fa1722a2fae8699f0b3c9de11eff41
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{modname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(isodate)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(azure-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Azure Storage Blobs client library for Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
