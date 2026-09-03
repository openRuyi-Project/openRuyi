# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           timefmt-go
%define go_import_path  github.com/itchyny/timefmt-go

Name:           go-github-itchyny-timefmt-go
Version:        0.1.8
Release:        %autorelease
Summary:        Date and time formatting and parsing library for Go
License:        MIT
URL:            https://github.com/itchyny/timefmt-go
#!RemoteAsset:  sha256:e2cfd4d9a90f95b01b636f425cbd4a5b94e5f98aac331a84e3e6c6a0c8c37be6
Source0:        https://github.com/itchyny/timefmt-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Timefmt-go provides efficient strftime- and strptime-compatible date and time
formatting and parsing functions implemented in pure Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
