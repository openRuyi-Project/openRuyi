# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sketches-go
%define go_import_path  github.com/DataDog/sketches-go

Name:           go-github-datadog-sketches-go
Version:        1.4.8
Release:        %autorelease
Summary:        Distributed quantile sketch implementations for Go
License:        Apache-2.0
URL:            https://github.com/DataDog/sketches-go
#!RemoteAsset:  sha256:0f13afc24a27304941829d34d16b3a46d0f214abbf314e20e608454d29e6ca6d
Source0:        https://github.com/DataDog/sketches-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
Sketches-go provides DDSketch implementations with relative-error quantile
guarantees and support for merging distributed sketches.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
