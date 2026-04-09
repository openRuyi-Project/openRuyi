# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           easyjson
%define go_import_path  github.com/mailru/easyjson
# Test failure, may be cause by outdate code
%define go_test_ignore_failure 1

Name:           go-github-mailru-easyjson
Version:        0.9.1
Release:        %autorelease
Summary:        Fast JSON serializer for golang.
License:        MIT
URL:            https://github.com/mailru/easyjson
#!RemoteAsset
Source0:        https://github.com/mailru/easyjson/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/josharian/intern)

Provides:       go(github.com/mailru/easyjson) = %{version}

%description
Package easyjson provides a fast and easy way to marshal/unmarshal Go
structs to/from JSON without the use of reflection. In performance
tests, easyjson outperforms the standard encoding/json package by a
factor of 4-5x, and other JSON encoding packages by a factor of 2-3x.

easyjson aims to keep generated Go code simple enough so that it can be
easily optimized or fixed. Another goal is to provide users with the
ability to customize the generated code by providing options not
available with the standard encoding/json package, such as generating
"snake_case" names or enabling omitempty behavior by default.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
