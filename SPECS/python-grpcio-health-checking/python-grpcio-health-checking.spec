# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>
%global srcname grpcio-health-checking
%global pypi_name grpcio_health_checking

Name:           python-%{srcname}
Version:        1.82.1
Release:        %autorelease
Summary:        Standard Health Checking Service for gRPC
License:        Apache-2.0
URL:            https://grpc.io/
VCS:            git:https://github.com/grpc/grpc
#!RemoteAsset:  sha256:86255e04e1d39f1c97a6632d41b63249351408de5c58e85eede87afd7d9828dd
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l grpc_health

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# The generated health service modules import grpc and protobuf at run time, and
# the import check loads them, so both have to be present while building.
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(protobuf)

Requires:       python3dist(grpcio)
Requires:       python3dist(protobuf)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Standard Health Checking Service for gRPC.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
