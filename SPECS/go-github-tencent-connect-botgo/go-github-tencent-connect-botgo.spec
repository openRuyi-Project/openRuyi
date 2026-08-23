# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           botgo
%define go_import_path  github.com/tencent-connect/botgo
# Skip API example and Redis-backed lock tests because they require network
# access, which the isolated OBS/CI build environment does not provide.
%define go_test_exclude %{shrink:
    %{go_import_path}/examples/apitest
    %{go_import_path}/sessions/remote/lock
}

Name:           go-github-tencent-connect-botgo
Version:        0.2.1
Release:        %autorelease
Summary:        Official Go SDK for QQ bots
License:        Apache-2.0
URL:            https://github.com/tencent-connect/botgo
#!RemoteAsset:  sha256:9a9d313afc3e9ea3b2c77dc022037080783ab1fec7e1d46cd4a7933599c7f496
Source0:        https://github.com/tencent-connect/botgo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects upstream non-constant and mismatched format strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-redis/redis/v8)
BuildRequires:  go(github.com/go-resty/resty/v2)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/zap/zapcore)

Provides:       go(github.com/tencent-connect/botgo) = %{version}

Requires:       go(github.com/go-redis/redis/v8)
Requires:       go(github.com/go-resty/resty/v2)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(go.uber.org/zap)
Requires:       go(go.uber.org/zap/zapcore)

%description
BotGo is the official Go SDK for building QQ bots, including authentication,
OpenAPI clients, event handling, WebSocket support, and webhook callbacks.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
