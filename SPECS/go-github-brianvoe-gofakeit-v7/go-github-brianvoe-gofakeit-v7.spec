# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gofakeit
%define go_import_path  github.com/brianvoe/gofakeit/v7

Name:           go-github-brianvoe-gofakeit-v7
Version:        7.15.0
Release:        %autorelease
Summary:        Random fake data generator written in go
License:        MIT
URL:            https://github.com/brianvoe/gofakeit
#!RemoteAsset:  sha256:c49fd88c590694cf1672849bdd519ec0ffd4f214954201edce38acc7e363dee3
Source0:        https://github.com/brianvoe/gofakeit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Golang 1.27 changes, we wait for upstream to fix the issue
BuildOption(check):  -skip '^(TestJSONRawMessage|TestJSONRawMessageWithTag|TestJSONRawMessageWithInvalidCustomFuncTag|ExampleImagePng|ExampleFaker_ImagePng)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/brianvoe/gofakeit/v7) = %{version}

%description
Random data generator written in go

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
