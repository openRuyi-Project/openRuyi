# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-grok
%define go_import_path  github.com/elastic/go-grok

Name:           go-github-elastic-go-grok
Version:        0.3.1
Release:        %autorelease
Summary:        Grok parser based on Go regular expressions
License:        Apache-2.0
URL:            https://github.com/elastic/go-grok
#!RemoteAsset:  sha256:358304966deab7db21e34f185ec48ff19d39ecaea94315af35726bcbe9d876ea
Source0:        https://github.com/elastic/go-grok/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/magefile/mage)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/trivago/grok)
BuildRequires:  go(github.com/vjeantet/grok)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/magefile/mage)

%description
This package parses structured fields from text using reusable Grok patterns
implemented with Go's regular expression engine.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
