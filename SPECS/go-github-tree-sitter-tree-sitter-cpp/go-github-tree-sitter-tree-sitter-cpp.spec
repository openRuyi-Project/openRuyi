# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tree-sitter-cpp
%define go_import_path  github.com/tree-sitter/tree-sitter-cpp

Name:           go-github-tree-sitter-tree-sitter-cpp
Version:        0.23.4
Release:        %autorelease
Summary:        C++ grammar for Tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter-cpp
#!RemoteAsset:  sha256:7a2c55afe3028f4105f25762ea58cc16537d1f5a1dcd9cca90410b3cd5d46051
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tree-sitter/go-tree-sitter)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/tree-sitter/go-tree-sitter)

%description
This package provides the Tree-sitter grammar for C++ and its Go bindings.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
