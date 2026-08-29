# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hcsshim
%define go_import_path  github.com/Microsoft/hcsshim

Name:           go-github-microsoft-hcsshim
Version:        0.11.7
Release:        %autorelease
Summary:        Containerd runhcs statistics types for Go
License:        MIT
URL:            https://github.com/Microsoft/hcsshim
#!RemoteAsset:  sha256:fb550edc6526403e5b897db2df9e38c216d90eb9d9768917e7d44d5479c76107
Source0:        https://github.com/Microsoft/hcsshim/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/cgroups)
BuildRequires:  go(github.com/gogo/protobuf)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/cmd/containerd-shim-runhcs-v1/stats) = %{version}

Requires:       go(github.com/containerd/cgroups)
Requires:       go(github.com/gogo/protobuf)

%description
This package provides the runhcs statistics types used by containerd's ctr
metrics command on Linux. The hcsshim executables themselves are Windows-only.

%prep -a
rm -rf vendor
# Linux ctr only imports the generated statistics types. Other hcsshim source
# and commands require Windows APIs and cannot be compiled on openRuyi.
find . -mindepth 1 -maxdepth 1 \
    ! -name go.mod ! -name go.sum ! -name LICENSE ! -name README.md ! -name cmd \
    -exec rm -rf {} +
find cmd -mindepth 1 -maxdepth 1 \
    ! -name containerd-shim-runhcs-v1 -exec rm -rf {} +
find cmd/containerd-shim-runhcs-v1 -mindepth 1 -maxdepth 1 \
    ! -name stats -exec rm -rf {} +

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
