# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>
%global srcname smg_grpc_servicer
%global pypi_name smg-grpc-servicer

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        %autorelease
Summary:        SMG gRPC servicer implementations for LLM inference engines
License:        Apache-2.0
URL:            https://github.com/smg-project/smg
VCS:            git:https://github.com/smg-project/smg.git
#!RemoteAsset:  sha256:1e3e18fe7db76bd4f320876366d14ba4cd2b5c0aea46c08c3457708cd6d95dbf
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Each engine integration imports its inference engine at module load time.
BuildOption(check):  -e 'smg_grpc_servicer.mlx*'
BuildOption(check):  -e 'smg_grpc_servicer.sglang*'
BuildOption(check):  -e 'smg_grpc_servicer.tokenspeed*'
BuildOption(check):  -e 'smg_grpc_servicer.vllm*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{pypi_name} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
This package provides gRPC servicer implementations for LLM inference engines,
including vLLM, MLX, TokenSpeed, and SGLang.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
