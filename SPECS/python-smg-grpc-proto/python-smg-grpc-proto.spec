# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>
%global srcname smg_grpc_proto
%global pypi_name smg-grpc-proto

Name:           python-%{pypi_name}
Version:        0.4.22
Release:        %autorelease
Summary:        Protocol Buffer definitions for SMG gRPC services
License:        Apache-2.0
URL:            https://github.com/smg-project/smg
VCS:            git:https://github.com/smg-project/smg.git
#!RemoteAsset:  sha256:0d69e782cabd4b76480461767351c2acddb887e2fed54bd1e7e4d1d4a52a5bd2
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# The build regenerates the .proto stubs in-tree, so the compiler side of the
# gRPC toolchain has to be present as well as the runtime.
BuildRequires:  python3dist(grpcio-tools)
BuildRequires:  python3dist(protobuf)

# The stubs are generated at build time by the distribution's grpcio-tools,
# whose protoc emits protobuf 7 code.
Requires:       python3dist(protobuf) >= 7.35.1

Provides:       python3-%{pypi_name} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
Protocol Buffer definitions and Python gRPC stubs for SMG (Shepherd Model
Gateway) services. The stubs are generated from the bundled .proto files when
the package is built.

%prep -a
# Upstream caps grpcio-tools below 1.82 only to keep protobuf 6 gencode for its
# protobuf 6 CI runtime. The distribution ships protobuf 7.
sed -i 's/"grpcio-tools>=1.81.1,<1.82"/"grpcio-tools>=1.81.1"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
