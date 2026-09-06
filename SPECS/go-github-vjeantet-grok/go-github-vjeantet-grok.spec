# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grok
%define go_import_path  github.com/vjeantet/grok

Name:           go-github-vjeantet-grok
Version:        1.0.1
Release:        %autorelease
Summary:        Grok pattern parser for Go
License:        Apache-2.0
URL:            https://github.com/vjeantet/grok
#!RemoteAsset:  sha256:f36b851686fc61b58dee9e15e24b2fe5eb3c75d4cfba98b27e443ddd51101806
Source0:        https://github.com/vjeantet/grok/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package extracts structured fields from text using reusable Grok
patterns and Go regular expressions.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
