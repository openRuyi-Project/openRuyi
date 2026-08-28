# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-logging
%define go_import_path  github.com/op/go-logging

Name:           go-github-op-go-logging
Version:        1
Release:        %autorelease
Summary:        Configurable logging infrastructure for Go
License:        BSD-3-Clause
URL:            https://github.com/op/go-logging
#!RemoteAsset:  sha256:949424f3ca0c1efbcc132bec73cc27b7bb426fad328f65605d7cf5403173d9bc
Source0:        https://github.com/op/go-logging/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep the legacy runtime call-path assertion stable under Go 1.26 by
# disabling compiler inlining for the test binary.
BuildOption(check):  -gcflags=all=-l

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
The logging package implements configurable loggers and backends for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
