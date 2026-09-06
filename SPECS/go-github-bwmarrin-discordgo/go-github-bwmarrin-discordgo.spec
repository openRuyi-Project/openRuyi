# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           discordgo
%define go_import_path  github.com/bwmarrin/discordgo
%define go_test_exclude_glob github.com/bwmarrin/discordgo/examples*

Name:           go-github-bwmarrin-discordgo
Version:        0.29.0
Release:        %autorelease
Summary:        Provides Discord binding for Go
License:        BSD-3-Clause
URL:            https://github.com/bwmarrin/discordgo
#!RemoteAsset:  sha256:70e819f60bae27eed689ebed82e58ebbdef8c0840777cf45ed94b5755665e173
Source0:        https://github.com/bwmarrin/discordgo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/bwmarrin/discordgo) = %{version}

Requires:       go(github.com/gorilla/websocket)
Requires:       go(golang.org/x/crypto)

%description
DiscordGo is a Go package providing low-level bindings to the Discord chat client API. It supports Discord API endpoints, WebSocket, and voice interfaces.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
