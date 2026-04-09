# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protobuf
%define go_import_path  github.com/golang/protobuf

Name:           go-github-golang-protobuf
Version:        1.5.4
Release:        %autorelease
Summary:        Go support for Google's protocol buffers
License:        BSD-3-Clause
URL:            https://github.com/golang/protobuf
#!RemoteAsset
Source0:        https://github.com/golang/protobuf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/golang/protobuf) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(google.golang.org/protobuf)

%description
This module (github.com/golang/protobuf
(https://pkg.go.dev/mod/github.com/golang/protobuf)) contains Go
bindings for protocol buffers.

It has been superseded by the google.golang.org/protobuf
(https://pkg.go.dev/mod/google.golang.org/protobuf) module, which
contains an updated and simplified API, support for protobuf reflection,
and many other improvements. We recommend that new code use the
google.golang.org/protobuf module.

Versions v1.4 and later of github.com/golang/protobuf are implemented in
terms of google.golang.org/protobuf. Programs which use both modules
must use at least version v1.4 of this one.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
