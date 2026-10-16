# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libtrust
%define go_import_path  github.com/docker/libtrust
%define commit_id       aabc10ec26b754e797f9028f4589c5b7bd90dc20

Name:           go-github-docker-libtrust
Version:        0+git20260922.aabc10e
Release:        %autorelease
Summary:        Public-key authentication and authorization for Go
License:        Apache-2.0
URL:            https://github.com/docker/libtrust
#!RemoteAsset:  sha256:f57dc468339505a0ce7f248cbec13af5fd492cd7a885c50af70d9786144f4f91
Source0:        https://github.com/docker/libtrust/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/docker/libtrust) = %{version}

%description
Public-key authentication and authorization for Go.

%prep -a
# These demonstrations define independent main functions in a single directory.
rm -rf tlsdemo

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
