# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clock
%define go_import_path  github.com/tilinna/clock

Name:           go-github-tilinna-clock
Version:        1.1.0
Release:        %autorelease
Summary:        Time mocking library for Go
License:        MIT
URL:            https://github.com/tilinna/clock
#!RemoteAsset:  sha256:e7c6f28341386ea4a8431564c64b7ba21ff99de0b14633f426f824fd9e7f5503
Source0:        https://github.com/tilinna/clock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Clock provides real-time and mock clock implementations for testing Go code,
including context-aware deadlines and timers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
