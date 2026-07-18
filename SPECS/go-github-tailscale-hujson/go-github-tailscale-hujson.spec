# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hujson
%define go_import_path  github.com/tailscale/hujson
%define commit_id       ecc657c15afd

Name:           go-github-tailscale-hujson
Version:        0+git20260718.ecc657c
Release:        %autorelease
Summary:        JSON for Humans (JWCC: JSON w/ comments and trailing commas)
License:        BSD-3-Clause
URL:            https://github.com/tailscale/hujson
#!RemoteAsset:  sha256:01816ec78930c869382f706d55a6375febdeb5c5108e9671bd3dd28ddb5964f8
Source0:        %{url}/archive/ecc657c15afd.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
# cmd/hujsonfmt is checked in GOPATH mode and imports gotextdiff. - Jvle
BuildRequires:  go(github.com/hexops/gotextdiff)

Provides:       go(github.com/tailscale/hujson) = %{version}
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/hexops/gotextdiff)

%description
The github.com/tailscale/hujson package implements the JWCC extension of standard JSON.

The JWCC format permits two things over standard JSON:

C-style line comments and block comments intermixed with whitespace,
allows trailing commas after the last member/element in an object/array.
All JSON is valid JWCC.

For details, see the JWCC docs at:

https://nigeltao.github.io/blog/2021/json-with-commas-comments.html

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
