# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cascadia
%define go_import_path  github.com/andybalholm/cascadia

Name:           go-github-andybalholm-cascadia
Version:        1.3.4
Release:        %autorelease
Summary:        CSS selector implementation for Go
License:        BSD-3-Clause
URL:            https://github.com/andybalholm/cascadia
#!RemoteAsset:  sha256:6d646174d19d2400b610d627ff43d4a53a4de91bfc02fad7a70aae73c36930e0
Source0:        https://codeload.github.com/andybalholm/cascadia/tar.gz/refs/tags/v%{version}#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/net)

%description
Cascadia implements CSS selectors for use with the Go HTML parser.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
