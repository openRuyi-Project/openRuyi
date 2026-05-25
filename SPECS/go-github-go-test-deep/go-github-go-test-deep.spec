# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           deep
%define go_import_path  github.com/go-test/deep

Name:           go-github-go-test-deep
Version:        1.1.1
Release:        %autorelease
Summary:        Golang deep variable equality test that returns human-readable differences
License:        MIT
URL:            https://github.com/go-test/deep
#!RemoteAsset:  sha256:ed08d8f98b4620637be97602d4c9e13c0b53e2347bb21a3a0a8f85ad9919b7dd
Source0:        https://github.com/go-test/deep/archive/refs/tags/v1.1.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n deep-1.1.1

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-test/deep) = %{version}
Provides:       go(github.com/go-test/deep/test/v1) = %{version}
Provides:       go(github.com/go-test/deep/test/v2) = %{version}


%description
Deep Variable Equality for Humans

[Image: Go Report Card] (https://goreportcard.com/badge/github.com/go-
test/deep) (https://goreportcard.com/report/github.com/go-test/deep)
[Image: Coverage Status] (https://coveralls.io/repos/github/go-
test/deep/badge.svg?branch=master) (https://coveralls.io/github/go-
test/deep?branch=master) [Image: Go Reference]
(https://pkg.go.dev/badge/github.com/go-test/deep.svg)
(https://pkg.go.dev/github.com/go-test/deep)

This package provides a single function: deep.Equal. It's like

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
