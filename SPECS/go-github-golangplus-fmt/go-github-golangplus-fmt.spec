# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fmt
%define go_import_path  github.com/golangplus/fmt
%define commit_id       2a5d6d7d2995baf7d847b7f16ac0179c6888d37b

Name:           go-github-golangplus-fmt
Version:        0+git20260922.2a5d6d7
Release:        %autorelease
Summary:        Formatting helpers for Go
License:        BSD-3-Clause
URL:            https://github.com/golangplus/fmt
#!RemoteAsset:  sha256:470fde1b55a0c3fcee8e39557448331928bc2ef9c28872b317c297c560a0f9ef
Source0:        https://github.com/golangplus/fmt/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golangplus/fmt) = %{version}

%description
This library adds formatting helpers for Go values and sequences.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
