# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testify
%define go_import_path  github.com/go-openapi/testify
# it says zero external dependencies but their tests depend too much dependencies - Julian
%define go_test_ignore_failure 1

Name:           go-github-go-openapi-testify
Version:        2.3.0
Release:        %autorelease
Summary:        Zero-dependency assertions library
License:        Apache-2.0
URL:            https://github.com/go-openapi/testify
#!RemoteAsset
Source0:        https://github.com/go-openapi/testify/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/go-openapi/testify) = %{version}

%description
A set of go packages that provide tools for testifying (verifying) that
your code behaves as you intended.

This is the go-openapi fork of the great testify
(https://github.com/stretchr/testify) package.

Main features:

 * zero external dependencies
 * opt-in dependencies for extra features (e.g. asserting YAML,
   colorized output)
 * assertions using generic types (see a basic example (https://go-
   openapi.github.io/testify#usage-with-generics)). Read the fully story
   with generics (https://go-openapi.github.io/testify/usage/generics)
 * searchable documentation (https://go-openapi.github.io/testify)

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
