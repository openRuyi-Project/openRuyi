# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-fuzz-headers
%define go_import_path  github.com/AdaLogics/go-fuzz-headers
%define commit_id e8a1dd7889d65b8a6f02175e0d79d7c0557db7f9

Name:           go-github-adalogics-go-fuzz-headers
Version:        0+git20260816.e8a1dd7
Release:        %autorelease
Summary:        This repository contains various helper functions for go fuzzing
License:        Apache-2.0
URL:            https://github.com/AdaLogics/go-fuzz-headers
#!RemoteAsset:  sha256:a8dbee5d0e350c46ca319ce75d6cc7ed9a0978d218d8917fb4073022a6c6754f
Source0:        https://github.com/AdaLogics/go-fuzz-headers/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/AdaLogics/go-fuzz-headers) = %{version}

%description
This repository contains various helper functions for go fuzzing. It is
mostly used in combination with go-fuzz but compatibility with fuzzing in
the standard library will also be supported. Any coverage guided fuzzing
engine that provides an array or slice of bytes can be used with go-fuzz-headers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
