# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           typescriptify-golang-structs
%define go_import_path  github.com/tkrajina/typescriptify-golang-structs

Name:           go-github-tkrajina-typescriptify-golang-structs
Version:        0.2.0
Release:        %autorelease
Summary:        Convert Go JSON structs to TypeScript models
License:        Apache-2.0
URL:            https://github.com/tkrajina/typescriptify-golang-structs
#!RemoteAsset:  sha256:0bc43bb0e4e70fb10402be448b58eae7babd19f69e9dcbf4ff77f8f62c1b8abc
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-test-generated-classes-with-modern-typescript.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tkrajina/go-reflector)
BuildRequires:  nodejs
BuildRequires:  typescript

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/tkrajina/go-reflector)

%description
This package provides a Go library for converting JSON-tagged Go structures
to TypeScript classes and interfaces.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
