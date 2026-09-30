# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           irc-go
%define go_import_path  github.com/ergochat/irc-go
# These tests need network access
%define go_test_exclude %{shrink:
    github.com/ergochat/irc-go/ircevent
    github.com/ergochat/irc-go/ircevent/examples
}

Name:           go-github-ergochat-irc-go
Version:        0.7.0
Release:        %autorelease
Summary:        Libraries for writing IRC clients and servers in Go
License:        ISC
URL:            https://github.com/ergochat/irc-go
#!RemoteAsset:  sha256:64626f3eb472782985bea2531e5936a57ace45568b2b8511c38578e35c412ce5
Source0:        https://github.com/ergochat/irc-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/ergochat/irc-go) = %{version}

Requires:       go(golang.org/x/net)

%description
Libraries for writing IRC clients and servers in Go, prioritizing correctness,
safety, and IRCv3 support. The APIs are not fully stable but are expected to change
only modestly.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
