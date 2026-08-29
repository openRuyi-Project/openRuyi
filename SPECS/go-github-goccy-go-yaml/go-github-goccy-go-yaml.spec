# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-yaml
%define go_import_path  github.com/goccy/go-yaml
# docs/playground is a demo command that pulls in go-graphviz and go-json; it is
# not needed for the library packages used by the test framework stack.
# - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}/docs/playground*

Name:           go-github-goccy-go-yaml
Version:        1.19.2
Release:        %autorelease
Summary:        YAML support library for Go
License:        MIT
URL:            https://github.com/goccy/go-yaml
#!RemoteAsset:  sha256:2cd611523019b61580a7f42056f92b1543c33f10bf5cda5d393608732577d6f9
Source0:        https://github.com/goccy/go-yaml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet reports Fatalf %q arguments with wrong static types in upstream
# decode tests; keep tests enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/go-playground/validator/v10)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/goccy/go-yaml) = %{version}

Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-colorable)

%description
This package provides YAML support library for Go.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
