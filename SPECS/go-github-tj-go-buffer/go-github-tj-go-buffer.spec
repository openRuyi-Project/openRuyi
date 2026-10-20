# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-buffer
%define go_import_path  github.com/tj/go-buffer

Name:           go-github-tj-go-buffer
Version:        1.2.0
Release:        %autorelease
Summary:        Batched buffers for Go
License:        MIT
URL:            https://github.com/tj/go-buffer
#!RemoteAsset:  sha256:a50c9a1f7a3dd0271c27b43910ee90abcd1b9f20e65b3427fe332316a52ad45c
Source0:        https://github.com/tj/go-buffer/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-buffer-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tj/assert)

Provides:       go(github.com/tj/go-buffer) = %{version}

%description
This package buffers entries and flushes batches when they reach a
configured size or interval.

%files
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
