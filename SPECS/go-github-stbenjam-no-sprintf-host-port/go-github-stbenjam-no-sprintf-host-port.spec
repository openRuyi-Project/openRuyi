# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           no-sprintf-host-port
%define go_import_path  github.com/stbenjam/no-sprintf-host-port

Name:           go-github-stbenjam-no-sprintf-host-port
Version:        0.3.1
Release:        %autorelease
Summary:        Go analyzer for unsafe host and port formatting
License:        MIT
URL:            https://github.com/stbenjam/no-sprintf-host-port
#!RemoteAsset:  sha256:426322fa7f939d0226c3736c914caf06a19a551afd22cfc5ae91e0628ce95bbe
Source0:        https://github.com/stbenjam/no-sprintf-host-port/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/stbenjam/no-sprintf-host-port) = %{version}
Provides:       go(github.com/stbenjam/no-sprintf-host-port/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for unsafe host and port formatting.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n no-sprintf-host-port-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/stbenjam/no-sprintf-host-port

%changelog
%autochangelog
