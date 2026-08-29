# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xstrings
%define go_import_path  github.com/huandu/xstrings

Name:           go-github-huandu-xstrings
Version:        1.5.0
Release:        %autorelease
Summary:        Is to provide string algorithms which are useful but not included in strings package
License:        MIT
URL:            https://github.com/huandu/xstrings
#!RemoteAsset:  sha256:2b242f966abe8aa75dbd6cf2c6625692feea117bc937b9f3fe76b99cdaf7365a
Source0:        https://github.com/huandu/xstrings/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/huandu/xstrings) = %{version}

%description
Go package xstrings (https://godoc.org/github.com/huandu/xstrings) is a
collection of string functions, which are widely used in other languages
but absent in Go package strings (http://golang.org/pkg/strings).

All functions are well tested and carefully tuned for performance.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
