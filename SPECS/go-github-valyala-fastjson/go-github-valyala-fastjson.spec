# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fastjson
%define go_import_path  github.com/valyala/fastjson

Name:           go-github-valyala-fastjson
Version:        1.6.10
Release:        %autorelease
Summary:        Fast JSON parser and validator for Go. No custom structs, no code generation, no reflection
License:        MIT
URL:            https://github.com/valyala/fastjson
#!RemoteAsset:  sha256:4e56f1d500e25bac7127c93bfbbf9deedfbec324c8b4b8e4c7a5e86091a05a95
Source0:        https://github.com/valyala/fastjson/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n fastjson-1.6.10

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/valyala/fastjson) = %{version}
Provides:       go(github.com/valyala/fastjson/fastfloat) = %{version}


%description
[Image: Build Status] (https://travis-ci.org/valyala/fastjson.svg)
(https://travis-ci.org/valyala/fastjson) [Image: GoDoc]
(https://godoc.org/github.com/valyala/fastjson?status.svg)
(http://godoc.org/github.com/valyala/fastjson) [Image: Go Report]
(https://goreportcard.com/badge/github.com/valyala/fastjson)
(https://goreportcard.com/report/github.com/valyala/fastjson) [Image:
codecov]
(https://codecov.io/gh/valyala/fastjson/branch/master/graph/badge.svg)
(https://codecov.io/gh/valyala/fastjson)

fastjson - fast JSON parser and validator for Go

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
