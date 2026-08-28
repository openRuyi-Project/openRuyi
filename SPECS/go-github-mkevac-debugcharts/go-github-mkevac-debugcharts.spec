# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           debugcharts
%define go_import_path  github.com/mkevac/debugcharts
%define commit_id       ae1c48aa8615ba68484030179fd93fe598f14694

Name:           go-github-mkevac-debugcharts
Version:        0+git20260818.ae1c48a
Release:        %autorelease
Summary:        Live runtime charts for Go applications
License:        MIT
URL:            https://github.com/mkevac/debugcharts
#!RemoteAsset:  sha256:fb02bf6123b894e24d8c7500319de4d80ba54366a0cc436bf9249061800f705c
Source0:        https://github.com/mkevac/debugcharts/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/StackExchange/wmi)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/gorilla/handlers)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/shirou/gopsutil)
BuildRequires:  go(github.com/shirou/w32)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/gorilla/handlers)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/shirou/gopsutil)

%description
Debugcharts exposes live charts for Go runtime memory use, garbage collection,
and operating-system metrics through an HTTP handler.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
