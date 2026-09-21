# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tree-sitter
%define go_import_path  github.com/tree-sitter/go-tree-sitter

Name:           go-github-tree-sitter-go-tree-sitter
Version:        0.25.0
Release:        %autorelease
Summary:        Go bindings for the Tree-sitter parsing library
License:        MIT
URL:            https://github.com/tree-sitter/go-tree-sitter
# Upstream removed the v0.25.0 Git tag after publishing the immutable Go
# module. The Go proxy records its Origin as commit adc13ffd8b2c0b01b878fda9f7c422ce0df5fad3.
#!RemoteAsset:  sha256:a2be3a1732377f427a97b3640739383585d46e14dc92637bfbd3d89dd2a9e6a7
Source0:        https://proxy.golang.org/%{go_import_path}/@v/v%{version}.zip#/%{_name}-%{version}.zip
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-pointer)
BuildRequires:  unzip

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/mattn/go-pointer)

%description
This package provides Go bindings for the Tree-sitter incremental parsing
library, including the C runtime sources required by cgo.

%prep
%setup -q -c -T
unzip -q %{SOURCE0}
cp -a "%{go_import_path}@v%{version}/." .
rm -rf github.com

%check
# Upstream tests import twelve grammar modules, including tree-sitter-cpp,
# which itself depends on this package. Skip those test-only modules to avoid
# an artificial bootstrap dependency cycle; the standard package build remains.
:

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
