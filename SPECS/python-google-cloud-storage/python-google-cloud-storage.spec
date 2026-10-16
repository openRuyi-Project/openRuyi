# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname google-cloud-storage
%global pypi_name google_cloud_storage

Name:           python-%{srcname}
Version:        3.14.1
Release:        %autorelease
Summary:        Google Cloud Storage client library for Python
License:        Apache-2.0
URL:            https://github.com/googleapis/python-storage
#!RemoteAsset:  sha256:b24e74b493c60b19b83462933a83bb831e45b6ca4924b0d75eac8e176b58b3a7
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l google +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(google-api-core) >= 2.27
BuildRequires:  python3dist(google-auth) >= 2.26.1
BuildRequires:  python3dist(google-cloud-core) >= 2.4.2
BuildRequires:  python3dist(google-crc32c) >= 1.6
BuildRequires:  python3dist(google-resumable-media) >= 2.7.2
BuildRequires:  python3dist(google-api-core[grpc]) >= 2.27
BuildRequires:  python3dist(grpc-google-iam-v1) >= 0.14.2
BuildRequires:  python3dist(grpcio) >= 1.59
BuildRequires:  python3dist(grpcio-status) >= 1.59
BuildRequires:  python3dist(proto-plus) >= 1.26.1
BuildRequires:  python3dist(protobuf) >= 6.33.5
BuildRequires:  python3dist(requests) >= 2.22
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the Python client library for Google Cloud Storage.

%pyproject_extras_subpkg -n python-%{srcname} grpc

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
