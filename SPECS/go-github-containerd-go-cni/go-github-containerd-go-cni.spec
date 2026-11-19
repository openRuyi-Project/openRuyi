# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cni
%define go_import_path  github.com/containerd/go-cni

Name:           go-github-containerd-go-cni
Version:        1.1.15
Release:        %autorelease
Summary:        Generic CNI library for Go
License:        Apache-2.0
URL:            https://github.com/containerd/go-cni
#!RemoteAsset:  sha256:f67576957a992199d0384185ade3a67723712e5277fe0e4f33a89a52ac5e9da5
Source0:        https://github.com/containerd/go-cni/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containernetworking/cni)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/containernetworking/cni)

%description
go-cni provides APIs for loading network configuration and setting up,
removing, and checking CNI plugin networks.

%prep -a
# The separate integration module needs network namespaces and installed CNI
# plugins. The root module has mock-based unit tests for the packaged library.
rm -rf integration

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
