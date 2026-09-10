# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           antlr
%define go_import_path  github.com/antlr4-go/antlr/v4

Name:           go-github-antlr4-go-antlr-v4
Version:        4.13.1
Release:        %autorelease
Summary:        ANTLR 4 runtime for Go
License:        BSD-3-Clause
URL:            https://github.com/antlr4-go/antlr
#!RemoteAsset:  sha256:2738fa0e68c3a61fea8de7b6c2f55fc1b39c7337a3d9351c2042bf6003e5590a
Source0:        https://codeload.github.com/antlr4-go/antlr/tar.gz/refs/tags/v%{version}#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/exp)

%description
This package provides the official ANTLR 4 runtime implementation for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
