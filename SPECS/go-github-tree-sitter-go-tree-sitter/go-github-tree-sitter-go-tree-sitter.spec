# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tree-sitter
%define go_import_path  github.com/tree-sitter/go-tree-sitter

Name:           go-github-tree-sitter-go-tree-sitter
Version:        0.24.0
Release:        %autorelease
Summary:        This repository contains Go bindings for the Tree-sitter parsing library
License:        MIT
URL:            https://github.com/tree-sitter/go-tree-sitter
#!RemoteAsset:  sha256:e3191517a20d38cae6600060f20463967a55ee3ae7f0f068a20482c079b74b61
Source0:        https://github.com/tree-sitter/go-tree-sitter/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-pointer)

Provides:       go(github.com/tree-sitter/go-tree-sitter) = %{version}

Requires:       go(github.com/mattn/go-pointer)

%description
Go bindings for the Tree-sitter incremental parsing library.

%check
%go_common
# Grammar tests depend on packages that themselves require these bindings.
# Compile a separate copy without those tests to bootstrap the provider;
# tree-sitter-cpp runs its upstream parser integration test against it.
cp -a . %{_builddir}/tree-sitter-check
find %{_builddir}/tree-sitter-check -name '*_test.go' -delete
cd %{_builddir}/tree-sitter-check
%{__go} test -v -short .

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
