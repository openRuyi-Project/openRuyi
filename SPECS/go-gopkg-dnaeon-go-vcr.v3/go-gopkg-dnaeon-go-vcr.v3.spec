# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-vcr
%define go_import_path  gopkg.in/dnaeon/go-vcr.v3

Name:           go-gopkg-dnaeon-go-vcr.v3
Version:        3.2.0
Release:        %autorelease
Summary:        Record and replay HTTP interactions in Go tests
License:        BSD-2-Clause
URL:            https://github.com/dnaeon/go-vcr
#!RemoteAsset:  sha256:831a1d236669511fbbd217478ae0927043bf738bc72fc32d9104b5df3d76934c
Source0:        https://github.com/dnaeon/go-vcr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use integer format verbs for HTTP status codes in tests.
Patch2000:      2000-fix-integer-status-format-verbs.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(gopkg.in/yaml.v3)

%description
Go-vcr records HTTP interactions and replays them to make tests deterministic
without repeatedly contacting external services.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
