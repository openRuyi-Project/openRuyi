# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stdr
%define go_import_path  github.com/go-logr/stdr
# ExampleNewWithOptions expects the older slog output format; Go 1.25 prints
# slog groups with '=' separators instead of ':' - HNO3Miracle
%define go_test_exclude %{go_import_path}

Name:           go-github-go-logr-stdr
Version:        1.2.2
Release:        %autorelease
Summary:        Logr implementation using the Go standard log package
License:        Apache-2.0
URL:            https://github.com/go-logr/stdr
#!RemoteAsset:  sha256:37d975b280d884ca0d55a800bc6e47314b6e86268e56254f9d15d19ca9404eb8
Source0:        https://github.com/go-logr/stdr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)

Provides:       go(github.com/go-logr/stdr) = %{version}

Requires:       go(github.com/go-logr/logr)

%description
This package provides a logr implementation backed by the Go standard
log package.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
