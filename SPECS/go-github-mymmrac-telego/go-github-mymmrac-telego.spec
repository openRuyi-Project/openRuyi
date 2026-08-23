# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           telego
%define go_import_path  github.com/mymmrac/telego
# TODO: Package missing example dependencies, including golang.ngrok.com/ngrok
# and github.com/gofiber/fiber/v3, then re-enable the excluded examples.
%define go_test_exclude %{shrink:
    github.com/mymmrac/telego/examples/menu_bot
    github.com/mymmrac/telego/examples/multi_bot_webhook_fiber
    github.com/mymmrac/telego/examples/ngrok
}

Name:           go-github-mymmrac-telego
Version:        1.7.0
Release:        %autorelease
Summary:        Telegram Bot API library for Go
License:        MIT
URL:            https://github.com/mymmrac/telego
#!RemoteAsset:  sha256:3fdaddfb2906a4eac8c227352c9c893d56a1264334c87922073d07a150437ce7
Source0:        https://github.com/mymmrac/telego/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/grbit/go-json)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/valyala/fasthttp)
BuildRequires:  go(github.com/valyala/fastjson)
BuildRequires:  go(go.uber.org/mock/gomock)

Provides:       go(github.com/mymmrac/telego) = %{version}

Requires:       go(github.com/grbit/go-json)
Requires:       go(github.com/valyala/fasthttp)
Requires:       go(github.com/valyala/fastjson)
Requires:       go(go.uber.org/mock/gomock)

%description
Telego provides a complete implementation of the Telegram Bot API, with Go
types and methods that closely match the upstream API.

%check -p
# GOPATH mode defaults to the legacy ServeMux behavior without a go directive.
export GODEBUG=httpmuxgo121=0

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
