# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fifo
%define go_import_path  github.com/containerd/fifo

Name:           go-github-containerd-fifo
Version:        1.1.0
Release:        %autorelease
Summary:        Go package for opening FIFOs safely
License:        Apache-2.0
URL:            https://github.com/containerd/fifo
#!RemoteAsset:  sha256:585203e9c55a39c1dbcee2fe1c0b84680f221b2ce6719b3254b1a94f1c618246
Source0:        https://github.com/containerd/fifo/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/containerd/fifo) = %{version}

Requires:       go(golang.org/x/sys)

%description
fifo provides safe helpers for opening named pipes in Go programs.
It is used by containerd to connect container I/O streams.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
