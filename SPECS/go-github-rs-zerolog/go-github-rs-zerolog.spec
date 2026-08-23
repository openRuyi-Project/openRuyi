# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zerolog
%define go_import_path  github.com/rs/zerolog
# Skip journald tests: write unixgram /run/systemd/journal/socket: no such file.
%define go_test_exclude github.com/rs/zerolog/journald

Name:           go-github-rs-zerolog
Version:        1.34.0
Release:        %autorelease
Summary:        Zero-allocation JSON logging library for Go
License:        MIT
URL:            https://github.com/rs/zerolog
#!RemoteAsset:  sha256:7a658d16b365f28fc6b75ae4ea2948cbe39e8fdaaadd0b5e92a6d911703ba430
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
