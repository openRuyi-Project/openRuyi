# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           line-bot-sdk-go
%define go_import_path  github.com/line/line-bot-sdk-go/v8

Name:           go-github-line-line-bot-sdk-go-v8
Version:        8.20.1
Release:        %autorelease
Summary:        LINE Messaging API SDK for Go
License:        Apache-2.0
URL:            https://github.com/line/line-bot-sdk-go
#!RemoteAsset:  sha256:a7f171a2e94e205823d2a105b7c59bb58c00b3641cd23887ff18db3b669d0c8b
Source0:        https://github.com/line/line-bot-sdk-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/line/line-bot-sdk-go/v8) = %{version}

%description
The LINE Messaging API SDK for Go makes it easy to develop bots using LINE
Messaging API, and you can create a sample bot within minutes.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
