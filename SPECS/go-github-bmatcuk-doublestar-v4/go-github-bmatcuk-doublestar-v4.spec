# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           doublestar
%define go_import_path  github.com/bmatcuk/doublestar/v4
# The examples module contains a non-constant fmt.Printf format rejected by
# the current Go vet; the library package itself remains fully tested.
%define go_test_exclude_glob %{go_import_path}/examples*

Name:           go-github-bmatcuk-doublestar-v4
Version:        4.10.0
Release:        %autorelease
Summary:        Path pattern matching and globbing supporting doublestar patterns
License:        MIT
URL:            https://github.com/bmatcuk/doublestar
#!RemoteAsset:  sha256:5d178e61fe67b3ae3ea46f023b2fbfaf0400e6ee74fe5cef1074690305a3f4f6
Source0:        https://github.com/bmatcuk/doublestar/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bmatcuk/doublestar/v4) = %{version}

%description
Doublestar provides path pattern matching and globbing with support for
doublestar (**) patterns.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
