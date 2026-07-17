# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fasthash
%define go_import_path  github.com/segmentio/fasthash

Name:           go-github-segmentio-fasthash
Version:        1.0.3
Release:        %autorelease
Summary:        Go package porting the standard hashing algorithms to a more efficient implementation
License:        MIT
URL:            https://github.com/segmentio/fasthash
#!RemoteAsset:  sha256:daadef14edb8643cddff971bd1ed5202aa1005a53cde1a6b81a3da68ca89eaf4
Source0:        https://github.com/segmentio/fasthash/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/segmentio/fasthash) = %{version}

%description
Go package porting the standard hashing algorithms to a more efficient
implementation.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
