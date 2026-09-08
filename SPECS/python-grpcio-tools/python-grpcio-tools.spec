# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname grpcio-tools
%global pypi_name grpcio_tools

Name:           python-%{srcname}
Version:        1.82.1
Release:        %autorelease
Summary:        Protobuf code generator for gRPC
License:        Apache-2.0
URL:            https://grpc.io/
VCS:            git:https://github.com/grpc/grpc.git
#!RemoteAsset:  sha256:2bd3176ccdbf7cd1f463eb75b7b83544c7d6429f5ca8a0f7f784b76097dac891
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l grpc_tools -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(grpcio)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
grpcio-tools provides the Protobuf compiler plugin for generating
gRPC Python code from service definitions.

%prep -a
sed -i 's/"Cython.*",/"Cython",/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/python-grpc-tools-protoc

%changelog
%autochangelog
