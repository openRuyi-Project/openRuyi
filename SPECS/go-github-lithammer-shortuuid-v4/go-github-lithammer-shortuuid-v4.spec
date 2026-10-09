# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           shortuuid
%define go_import_path  github.com/lithammer/shortuuid/v4

Name:           go-github-lithammer-shortuuid-v4
Version:        4.3.0
Release:        %autorelease
Summary:        Concise URL-safe UUIDs for Go
License:        MIT
URL:            https://github.com/lithammer/shortuuid
#!RemoteAsset:  sha256:74228fcf34976b4c1d4804b054496ccb1475d2aa3860a23fda5d767c70d2595c
Source0:        https://github.com/lithammer/shortuuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/uuid)

Provides:       go(github.com/lithammer/shortuuid/v4) = %{version}

Requires:       go(github.com/google/uuid)

%description
shortuuid/v4 generates concise, unambiguous, URL-safe UUIDs. MinIO uses
the v4 import path; the unversioned shortuuid package is already in the
distro.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
