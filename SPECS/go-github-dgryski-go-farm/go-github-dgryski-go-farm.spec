# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-farm
%define go_import_path  github.com/dgryski/go-farm
%define commit_id       3414d57e47dafc94b763b0f8a0470333f5f44051

Name:           go-github-dgryski-go-farm
Version:        0+git20260817.3414d57
Release:        %autorelease
Summary:        FarmHash hash functions implemented in Go
License:        MIT
URL:            https://github.com/dgryski/go-farm
#!RemoteAsset:  sha256:15c84a30ae3984562d9cf071e69d64dfa515b93ab8e69012f4b67ec6f0e7964f
Source0:        https://github.com/dgryski/go-farm/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Go-farm provides a Go implementation of Google's non-SSE4 and non-AESNI
FarmHash functions.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
