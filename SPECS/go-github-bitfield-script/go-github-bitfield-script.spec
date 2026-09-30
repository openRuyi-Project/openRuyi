# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           script
%define go_import_path  github.com/bitfield/script

Name:           go-github-bitfield-script
Version:        0.25.0
Release:        %autorelease
Summary:        Shell-like pipelines for Go
License:        MIT
URL:            https://github.com/bitfield/script
#!RemoteAsset:  sha256:ff389efa4cdbd449ce52329cfb57a92250a8d02b396b31d28ec5d572fc0f04c5
Source0:        https://github.com/bitfield/script/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/itchyny/gojq)
BuildRequires:  go(github.com/itchyny/timefmt-go)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(mvdan.cc/sh/v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/itchyny/gojq)
Requires:       go(mvdan.cc/sh/v3)

%description
Script builds shell-like data-processing pipelines in Go for reading files,
running commands, filtering text, and transforming streams.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
