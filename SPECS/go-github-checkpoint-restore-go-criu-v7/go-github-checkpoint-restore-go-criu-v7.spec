# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-criu
%define go_import_path  github.com/checkpoint-restore/go-criu/v7
# The upstream source archive omits crit/test-imgs required by its tests.
%global go_test_ignore_failure 1

Name:           go-github-checkpoint-restore-go-criu-v7
Version:        7.2.0
Release:        %autorelease
Summary:        This repository provides Go bindings for CRIU
License:        Apache-2.0
URL:            https://github.com/checkpoint-restore/go-criu
#!RemoteAsset:  sha256:fe6e0a3747ebed21ef6fc03e93967cafdebeac54d8b17a7469310676a1b03141
Source0:        https://github.com/checkpoint-restore/go-criu/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/checkpoint-restore/go-criu/v7) = %{version}

Requires:       go(github.com/spf13/cobra)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description
This repository provides Go bindings for CRIU. The code is based on the
Go-based PHaul implementation from the CRIU repository and has been moved
to this repository for easier inclusion in Go projects.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
