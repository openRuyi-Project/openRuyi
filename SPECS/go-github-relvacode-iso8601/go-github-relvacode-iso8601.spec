# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           iso8601
%define go_import_path  github.com/relvacode/iso8601

Name:           go-github-relvacode-iso8601
Version:        1.8.0
Release:        %autorelease
Summary:        ISO 8601 date and time parser for Go
License:        MIT
URL:            https://github.com/relvacode/iso8601
VCS:            git:https://github.com/relvacode/iso8601.git
#!RemoteAsset:  sha256:1630eacfc4862cd49ed7bc44790ffe65747ff0f2d648ec87bbebfc2b73601e1a
Source0:        https://github.com/relvacode/iso8601/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This library parses ISO 8601 dates and times into Go time values without
regular expressions. It also provides a time type for JSON decoding.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
