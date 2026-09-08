# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           slack
%define go_import_path  github.com/slack-go/slack
# Skip flaky RTM disconnect test package: timed out waiting for disconnect.
%define go_test_exclude %{go_import_path}

Name:           go-github-slack-go-slack
Version:        0.29.0
Release:        %autorelease
Summary:        Go client library for the Slack API
License:        BSD-2-Clause
URL:            https://github.com/slack-go/slack
#!RemoteAsset:  sha256:696fed6a80750da33a040aa7ae3eb73f39b42bdf85dabb90094c7c8e463a1286
Source0:        https://github.com/slack-go/slack/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects upstream non-constant and mismatched format strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/slack-go/slack) = %{version}

Requires:       go(github.com/gorilla/websocket)

%description
Slack-go provides access to Slack REST APIs and the Real-Time Messaging
protocol over WebSocket from Go applications.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
