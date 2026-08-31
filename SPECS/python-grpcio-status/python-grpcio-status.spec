# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname grpcio-status
%global pypi_name grpcio_status

Name:           python-%{srcname}
Version:        1.82.1
Release:        %autorelease
Summary:        Status proto mapping for gRPC
License:        Apache-2.0
URL:            https://grpc.io/
VCS:            git:https://github.com/grpc/grpc.git
#!RemoteAsset:  sha256:d9de8ac34763cd468130fdd2923294af7c3d28d09426f6c45221d27c25931130
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l grpc_status

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(googleapis-common-protos)
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
grpcio-status provides a mapping between rich Protobuf status messages and
gRPC status codes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
