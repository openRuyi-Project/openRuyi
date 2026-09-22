# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bytes
%define go_import_path  github.com/golangplus/bytes
%define commit_id       45c989fe545070ef7c9003cf1998bb195c61731a

Name:           go-github-golangplus-bytes
Version:        0+git20260922.45c989f
Release:        %autorelease
Summary:        Byte slice utilities for Go
License:        BSD-3-Clause
URL:            https://github.com/golangplus/bytes
#!RemoteAsset:  sha256:cb706b4294713f66d67baa3e202202cf69b46510f1b7144df213a08e64ed61fa
Source0:        https://github.com/golangplus/bytes/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golangplus/testing)

Provides:       go(github.com/golangplus/bytes) = %{version}

%description
This library extends byte slices with readers, writers and numeric formatting.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
