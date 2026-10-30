# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gotestingmock
%define go_import_path  github.com/newmo-oss/gotestingmock

Name:           go-github-newmo-oss-gotestingmock
Version:        0.2.0
Release:        %autorelease
Summary:        Mock testing helpers for Go
License:        MIT
URL:            https://github.com/newmo-oss/gotestingmock
#!RemoteAsset:  sha256:417cb22fce2e690ca2258bde31eec05431a8301fd753efa12829214efdbb3887
Source0:        https://github.com/newmo-oss/gotestingmock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/newmo-oss/go-caller)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/newmo-oss/go-caller)

%description
gotestingmock provides testing helpers for running and observing Go test
functions in isolated goroutines.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
