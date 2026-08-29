# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-criu
%define go_import_path  github.com/checkpoint-restore/go-criu/v8
# crit tests require CRIU image fixtures absent from the upstream release archive.
# - Jvle
%define go_test_exclude  github.com/checkpoint-restore/go-criu/v8/crit

Name:           go-github-checkpoint-restore-go-criu-v8
Version:        8.4.0
Release:        %autorelease
Summary:        This repository provides Go bindings for CRIU
License:        Apache-2.0
URL:            https://github.com/checkpoint-restore/go-criu
#!RemoteAsset:  sha256:8b79941af08f0ab408d11132133e7dc7ee7c38022a5f8c8e8e77ae59cdde20f6
Source0:        https://github.com/checkpoint-restore/go-criu/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aperturerobotics/protobuf-go-lite)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/checkpoint-restore/go-criu/v8) = %{version}

Requires:       go(github.com/aperturerobotics/protobuf-go-lite)
Requires:       go(github.com/spf13/cobra)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description
without the need to set up all the infrastructure to make the actual RPC
The Go bindings provide an easy way to use the CRIU RPC calls from Go
connection to CRIU.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
