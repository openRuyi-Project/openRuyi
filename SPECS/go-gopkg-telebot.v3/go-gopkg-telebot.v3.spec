# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           telebot
%define go_import_path  gopkg.in/telebot.v3

Name:           go-gopkg-telebot.v3
Version:        3.3.8
Release:        %autorelease
Summary:        Telegram Bot API framework for Go
License:        MIT
URL:            https://github.com/tucnak/telebot
#!RemoteAsset:  sha256:cddace7f57ab607eb4273ec0eb1357f983d6dd2b299e4f04afaa508581ae6743
Source0:        https://github.com/tucnak/telebot/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(gopkg.in/telebot.v3) = %{version}

Requires:       go(github.com/goccy/go-yaml)
Requires:       go(github.com/spf13/viper)

%description
Telebot is a framework for building Telegram bots in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
