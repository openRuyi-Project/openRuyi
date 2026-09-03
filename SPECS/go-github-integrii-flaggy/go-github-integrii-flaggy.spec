# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           flaggy
%define go_import_path  github.com/integrii/flaggy

Name:           go-github-integrii-flaggy
Version:        1.8.0
Release:        %autorelease
Summary:        Idiomatic Go input parsing with subcommands, positional values, and flags at any position.
License:        Unlicense
URL:            https://github.com/integrii/flaggy
#!RemoteAsset:  sha256:c2d761b970fe24ae291f997a1edf931db678a24f01a88c50b8cf080efc259b6f
Source0:        https://github.com/integrii/flaggy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/integrii/flaggy) = %{version}

%description
flaggy is a Go command-line flag parser with support for subcommands and positional values.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
