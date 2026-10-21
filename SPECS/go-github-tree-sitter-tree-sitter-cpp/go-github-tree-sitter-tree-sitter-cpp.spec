# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tree-sitter-cpp
%define go_import_path  github.com/tree-sitter/tree-sitter-cpp

Name:           go-github-tree-sitter-tree-sitter-cpp
Version:        0.23.4
Release:        %autorelease
Summary:        C++ grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter-cpp
#!RemoteAsset:  sha256:7a2c55afe3028f4105f25762ea58cc16537d1f5a1dcd9cca90410b3cd5d46051
Source0:        https://github.com/tree-sitter/tree-sitter-cpp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tree-sitter/go-tree-sitter)

Provides:       go(github.com/tree-sitter/tree-sitter-cpp) = %{version}

%description
tree-sitter-cpp provides a C++ grammar for the Tree-sitter incremental
parsing library. This package contains the grammar sources and Go bindings
for parsing C++ source code from Go programs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
