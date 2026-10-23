# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           discordgo-fork
%define commit_id       e8e546f5d532af6106128821254ceb4936e1fd07
%define go_import_path  github.com/bwmarrin/discordgo
%define go_test_exclude_glob github.com/bwmarrin/discordgo/examples*

Name:           go-github-yeongaori-discordgo-fork
Version:        0+git20260319.e8e546f
Release:        %autorelease
Summary:        DiscordGo fork with DAVE voice protocol support
License:        BSD-3-Clause
URL:            https://github.com/yeongaori/discordgo-fork
#!RemoteAsset:  sha256:936115c56d7cd80fe33ab93c06d633d06b88c984e45b2c79d6a51419555d7d4b
Source0:        https://github.com/yeongaori/discordgo-fork/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/bwmarrin/discordgo) = %{version}

Conflicts:      go-github-bwmarrin-discordgo

Requires:       go(github.com/cloudflare/circl)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(golang.org/x/crypto)

%description
This fork of DiscordGo adds DAVE encrypted voice support and context-aware
voice connection methods while retaining the original Go import path.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
