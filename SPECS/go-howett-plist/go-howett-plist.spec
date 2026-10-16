# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           plist
%define go_import_path  howett.net/plist

Name:           go-howett-plist
Version:        1.0.0
Release:        %autorelease
Summary:        Apple property list encoding and decoding for Go
License:        BSD-2-Clause
URL:            https://github.com/DHowett/go-plist
#!RemoteAsset:  sha256:213b3f1d54c3bff8ce3e2b2782ca95a13faf26d4bc6475234d3f614732fedd4a
Source0:        https://github.com/DHowett/go-plist/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Legacy parser error helpers fail the dynamic-format go vet check.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(howett.net/plist) = %{version}

%description
Encode and decode Apple property lists in binary, XML and text formats.

%prep -a
# Optional command-line converters require unrelated flag and YAML packages.
rm -rf cmd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
