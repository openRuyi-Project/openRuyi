# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           iso8601
%define go_import_path  github.com/relvacode/iso8601

Name:           go-github-relvacode-iso8601
Version:        1.7.0
Release:        %autorelease
Summary:        ISO 8601 date and time parser for Go
License:        MIT
URL:            https://github.com/relvacode/iso8601
VCS:            git:https://github.com/relvacode/iso8601.git
#!RemoteAsset:  sha256:61c49316738b649bccea5768788883ca5c18ddde3adb2b8ca587f0143fee6659
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
