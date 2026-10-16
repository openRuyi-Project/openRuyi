# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname google-cloud-core
%global pypi_name google_cloud_core

Name:           python-%{srcname}
Version:        2.7.0
Release:        %autorelease
Summary:        Core helpers for Google Cloud client libraries
License:        Apache-2.0
URL:            https://github.com/googleapis/python-cloud-core
#!RemoteAsset:  sha256:874aaf89765db87a9b911b7a2ca7c5068554868eed9e75c7766affe342a2913d
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l google +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(google-api-core) >= 2.28
BuildRequires:  python3dist(google-auth) >= 2.14.1
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Google Cloud Core provides common base classes and helpers for Google Cloud
Python client libraries.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
