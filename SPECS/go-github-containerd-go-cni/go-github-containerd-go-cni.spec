# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cni
%define go_import_path  github.com/containerd/go-cni

Name:           go-github-containerd-go-cni
Version:        1.1.9
Release:        %autorelease
Summary:        Generic CNI library for Go
License:        Apache-2.0
URL:            https://github.com/containerd/go-cni
#!RemoteAsset:  sha256:c0ad26845675d473e130452a6f4c9eed7f91dab56c0d12f0c7f97711f9a918a1
Source0:        https://github.com/containerd/go-cni/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containernetworking/cni)
BuildRequires:  go(github.com/stretchr/testify)

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
