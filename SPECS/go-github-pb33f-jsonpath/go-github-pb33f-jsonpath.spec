# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonpath
%define go_import_path  github.com/pb33f/jsonpath
# Upstream release tarball does not include jsonpath-compliance-test-suite/cts.json,
# so root package tests fail before exercising package code - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}*

Name:           go-github-pb33f-jsonpath
Version:        0.8.2
Release:        %autorelease
Summary:        JSONPath implementation for Go
License:        Apache-2.0
URL:            https://github.com/pb33f/jsonpath
#!RemoteAsset:  sha256:0fbf47e08ada6ce5e9b1b155a85fcae429c64b8dbeb6326fe915793a50813b5b
Source0:        https://github.com/pb33f/jsonpath/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/pb33f/jsonpath) = %{version}

Requires:       go(go.yaml.in/yaml/v4)

%description
JSONPath implementation for Go with JSONPath Plus extensions.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
