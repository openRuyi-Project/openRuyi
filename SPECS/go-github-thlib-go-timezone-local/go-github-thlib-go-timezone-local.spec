# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-timezone-local
%define go_import_path  github.com/thlib/go-timezone-local
%define commit_id       ef149e42d28e01293e9ebda9f3d377283b84b9c0

Name:           go-github-thlib-go-timezone-local
Version:        0+git20260723.ef149e4
Release:        %autorelease
Summary:        Local timezone name detection for Go
License:        Unlicense
URL:            https://github.com/thlib/go-timezone-local
#!RemoteAsset:  sha256:00b9380fd2a3a1fd4c70120da8ed399d8d5004cdc7d014b011b8d70b4e5b64ef
Source0:        https://github.com/thlib/go-timezone-local/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/thlib/go-timezone-local) = %{version}

%description
go-timezone-local detects the canonical name of the operating system's local
timezone for use by Go applications.

%check
# Compile all packages and tests before tolerating tzdata updater tests that
# require ftp.iana.org and raw.githubusercontent.com network access.
%buildsystem_golangmodules_check -run '^$'
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
