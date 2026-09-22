# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-lz4
%define go_import_path  github.com/bkaradzic/go-lz4

Name:           go-github-bkaradzic-go-lz4
Version:        1.0.0
Release:        %autorelease
Summary:        LZ4 compression and decompression for Go
License:        BSD-2-Clause
URL:            https://github.com/bkaradzic/go-lz4
#!RemoteAsset:  sha256:d45102ed9967e7f371844b04a9d66b48f9a11aad2238591c711c8819748afa94
Source0:        https://github.com/bkaradzic/go-lz4/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bkaradzic/go-lz4) = %{version}

%description
This library implements LZ4 block compression, readers and writers in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
