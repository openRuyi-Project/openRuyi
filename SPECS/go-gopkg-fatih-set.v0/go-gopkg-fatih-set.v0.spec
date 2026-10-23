# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           set
%define go_import_path  gopkg.in/fatih/set.v0

# Examples still import the old github.com/fatih/set path. The library uses
# gopkg.in/fatih/set.v0 and its full test suite remains enabled.
%define go_test_exclude_glob %{go_import_path}/examples*

Name:           go-gopkg-fatih-set.v0
Version:        0.2.1
Release:        %autorelease
Summary:        Thread-safe and basic set types for Go
License:        MIT
URL:            https://github.com/fatih/set
#!RemoteAsset:  sha256:8b1d0bf1529083f9c29cf82e5c8419d8705797c4470a41ec74cf4d4dd373622f
Source0:        https://github.com/fatih/set/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(gopkg.in/fatih/set.v0) = %{version}

%description
This library provides hash-based set implementations with optional
thread safety. Cloudmux uses the historical gopkg.in/fatih/set.v0 path.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
