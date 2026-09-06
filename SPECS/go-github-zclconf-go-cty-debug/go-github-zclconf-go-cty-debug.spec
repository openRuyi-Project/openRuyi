# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cty-debug
%define go_import_path  github.com/zclconf/go-cty-debug
%define commit_id       0d6042c539401a57fc0cca85ded2861d4a5173c4

Name:           go-github-zclconf-go-cty-debug
Version:        0+git20260819.0d6042c
Release:        %autorelease
Summary:        Debugging and inspection utilities for cty
License:        MIT
URL:            https://github.com/zclconf/go-cty-debug
#!RemoteAsset:  sha256:dc98b5561061754fdae18374e7a596ea473d3bda11e27bfb1f2011b32ba37732
Source0:        https://github.com/zclconf/go-cty-debug/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/zclconf/go-cty)
BuildRequires:  go(golang.org/x/text)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/zclconf/go-cty)
Requires:       go(golang.org/x/text)

%description
Go-cty-debug provides debugging and inspection helpers for cty values and
types.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
