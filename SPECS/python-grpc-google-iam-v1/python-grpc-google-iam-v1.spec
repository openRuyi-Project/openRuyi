# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname grpc-google-iam-v1
%global pypi_name grpc_google_iam_v1

Name:           python-%{srcname}
Version:        0.14.5
Release:        %autorelease
Summary:        Google IAM API protocol definitions for Python
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python
#!RemoteAsset:  sha256:07fd3a9fafb586588e771831fbfc8f6597050181d0c3b45e039d18b8fdc1aab5
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l google +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(googleapis-common-protos[grpc]) >= 1.69.2
BuildRequires:  python3dist(grpcio) >= 1.59
BuildRequires:  python3dist(protobuf) >= 6.33.5
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides generated Python protocol definitions for the Google
IAM v1 API.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
