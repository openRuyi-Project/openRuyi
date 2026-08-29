# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goxml2json
%define go_import_path  github.com/basgys/goxml2json

Name:           go-github-basgys-goxml2json
Version:        1.1.0
Release:        %autorelease
Summary:        XML to JSON converter written in Go (no schema, no structs)
License:        MIT
URL:            https://github.com/basgys/goxml2json
#!RemoteAsset:  sha256:8f76246cd0d4202f52495d54b04cb990e7dc643242b6d46638d73eda9369e62e
Source0:        https://github.com/basgys/goxml2json/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bitly/go-simplejson)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/basgys/goxml2json) = %{version}

Requires:       go(golang.org/x/net)

%description
goxml2json converts XML documents into JSON without requiring schemas or Go
struct definitions.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
