# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           btrfs
%define go_import_path  github.com/containerd/btrfs/v2

Name:           go-github-containerd-btrfs-v2
Version:        2.0.0
Release:        %autorelease
Summary:        Provides bindings for working with btrfs partitions from Go
License:        Apache-2.0
URL:            https://github.com/containerd/btrfs
#!RemoteAsset:  sha256:d19f38a7237bfdd318c674b68c109b5fa3dc1392225018bded14076f18cd8856
Source0:        https://github.com/containerd/btrfs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/containerd/btrfs/v2) = %{version}

Requires:       go(golang.org/x/sys)

%description
Native Go bindings for btrfs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
