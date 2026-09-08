# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zerolog
%define go_import_path  github.com/rs/zerolog
# Skip journald tests: write unixgram /run/systemd/journal/socket: no such file.
%define go_test_exclude github.com/rs/zerolog/journald

Name:           go-github-rs-zerolog
Version:        1.35.1
Release:        %autorelease
Summary:        Zero-allocation JSON logging library for Go
License:        MIT
URL:            https://github.com/rs/zerolog
#!RemoteAsset:  sha256:10f3751ea3b5fde2cdf217e0789711bb078bb4caf3909ac1307ff6c35292f8c7
Source0:        https://github.com/rs/zerolog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/rs/xid)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/rs/zerolog) = %{version}

Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/rs/xid)
Requires:       go(golang.org/x/tools)

%description
Zerolog provides fast structured logging dedicated to JSON output. Its chained
API avoids allocations and reflection when writing log events.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
