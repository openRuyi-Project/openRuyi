# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grok
%define go_import_path  github.com/trivago/grok

Name:           go-github-trivago-grok
Version:        1.0.0
Release:        %autorelease
Summary:        Concurrent Grok parser for Go
License:        Apache-2.0
URL:            https://github.com/trivago/grok
#!RemoteAsset:  sha256:bf9113d5206444fbc0826d57c235486a5fa89cbe42556fb2726494ac0c2197b8
Source0:        https://github.com/trivago/grok/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/trivago/tgo)

Provides:       go(%{go_import_path}) = %{version}

%description
This package parses Grok patterns without shared locks and provides reusable
pattern sets for concurrent Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
