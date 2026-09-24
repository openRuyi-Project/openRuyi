# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname google-api-core
%global pypi_name google_api_core

Name:           python-%{srcname}
Version:        2.37.0
Release:        %autorelease
Summary:        Core helpers for Google API client libraries
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-api-core
#!RemoteAsset:  sha256:cf58f220aa797f1ffdda52194c4c7d72efeced09297c2976529f8135f6d85b9a
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l google +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(google-auth) >= 2.14.1
BuildRequires:  python3dist(googleapis-common-protos) >= 1.69.2
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(opentelemetry-api) >= 1.44
BuildRequires:  python3dist(proto-plus) >= 1.26.1
BuildRequires:  python3dist(protobuf) >= 6.33.5
BuildRequires:  python3dist(requests) >= 2.33
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Google API Core contains common helpers shared by Google Cloud Python client
libraries.

%pyproject_extras_subpkg -n python-%{srcname} grpc

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
