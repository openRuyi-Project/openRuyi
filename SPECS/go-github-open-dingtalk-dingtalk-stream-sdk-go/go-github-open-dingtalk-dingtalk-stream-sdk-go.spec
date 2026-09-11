# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dingtalk-stream-sdk-go
%define go_import_path  github.com/open-dingtalk/dingtalk-stream-sdk-go

Name:           go-github-open-dingtalk-dingtalk-stream-sdk-go
Version:        0.9.1
Release:        %autorelease
Summary:        Go SDK for the DingTalk Stream Mode API
License:        MIT
URL:            https://github.com/open-dingtalk/dingtalk-stream-sdk-go
#!RemoteAsset:  sha256:00136c78a8da16378dd46ca3ea915003b2a02f327bfd10f4a1338f8d26aa4eb9
Source0:        https://github.com/open-dingtalk/dingtalk-stream-sdk-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix go vet: non-constant format string in call to fmt.Errorf.
Patch2000:      2000-chatbot-preserve-error-response-text.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/open-dingtalk/dingtalk-stream-sdk-go) = %{version}

Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gorilla/websocket)

%description
Go SDK for receiving DingTalk events, chatbot messages and card callbacks
through Stream Mode without a public webhook endpoint.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
