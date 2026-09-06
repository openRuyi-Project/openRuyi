# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           murmur3
%define go_import_path  github.com/twmb/murmur3

Name:           go-github-twmb-murmur3
Version:        1.1.8
Release:        %autorelease
Summary:        MurmurHash3 implementation for Go
License:        BSD-3-Clause
URL:            https://github.com/twmb/murmur3
#!RemoteAsset:  sha256:afa51249308db62b5a2d4610b7c30cd41dc4906777211d8d8b09250875a668aa
Source0:        https://github.com/twmb/murmur3/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package implements streaming 32-bit, 64-bit, and 128-bit MurmurHash3
functions with portable Go and optimized amd64 assembly.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
