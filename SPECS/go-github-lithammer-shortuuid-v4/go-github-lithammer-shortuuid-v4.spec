# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           shortuuid
%define go_import_path  github.com/lithammer/shortuuid/v4

Name:           go-github-lithammer-shortuuid-v4
Version:        4.2.0
Release:        %autorelease
Summary:        Concise URL-safe UUIDs for Go
License:        MIT
URL:            https://github.com/lithammer/shortuuid
#!RemoteAsset:  sha256:7ede63e386da63a9da2e085e2a938079d4cd2e9de329024ea30f4838abb916fa
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
