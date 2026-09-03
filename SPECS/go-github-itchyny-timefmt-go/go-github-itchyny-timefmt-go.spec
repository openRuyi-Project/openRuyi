# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           timefmt-go
%define go_import_path  github.com/itchyny/timefmt-go

Name:           go-github-itchyny-timefmt-go
Version:        0.1.5
Release:        %autorelease
Summary:        Efficient strftime and strptime implementation for Go
License:        MIT
URL:            https://github.com/itchyny/timefmt-go
#!RemoteAsset:  sha256:158ee59ce39ad65b7078bc354b266d0d08eabdb529cb54e78f0b158dbd836bf4
Source0:        https://github.com/itchyny/timefmt-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/itchyny/timefmt-go) = %{version}

%description
timefmt-go provides efficient strftime-compatible formatting and
strptime-compatible parsing for Go time values.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
