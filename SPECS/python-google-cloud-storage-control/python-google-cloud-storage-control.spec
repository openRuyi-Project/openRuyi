# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname google-cloud-storage-control
%global pypi_name google_cloud_storage_control

Name:           python-%{srcname}
Version:        1.15.0
Release:        %autorelease
Summary:        Google Cloud Storage Control client library for Python
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storage-control
#!RemoteAsset:  sha256:e3d50276f0aed0c33ebcf3c6221e933889e042df70a56886ddffe59c66889183
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l google +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(google-api-core[grpc]) >= 2.28
BuildRequires:  python3dist(google-auth) >= 2.14.1
BuildRequires:  python3dist(grpc-google-iam-v1) >= 0.14.2
BuildRequires:  python3dist(grpcio) >= 1.59
BuildRequires:  python3dist(proto-plus) >= 1.26.1
BuildRequires:  python3dist(protobuf) >= 6.33.5
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the Python client for the Google Cloud Storage Control
API.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
