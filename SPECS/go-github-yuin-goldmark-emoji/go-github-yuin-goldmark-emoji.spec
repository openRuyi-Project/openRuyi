# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goldmark-emoji
%define go_import_path  github.com/yuin/goldmark-emoji

Name:           go-github-yuin-goldmark-emoji
Version:        1.0.6
Release:        %autorelease
Summary:        Emoji extension for the Goldmark Markdown parser
License:        MIT
URL:            https://github.com/yuin/goldmark-emoji
#!RemoteAsset:  sha256:18d7b88aa782ae3d0e8f885c86d33097245254e9c4c60921aae5735a3df3ec3d
Source0:        https://github.com/yuin/goldmark-emoji/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/yuin/goldmark)

Provides:       go(github.com/yuin/goldmark-emoji) = %{version}

Requires:       go(github.com/yuin/goldmark)

%description
goldmark-emoji adds GitHub-style emoji shortcode parsing and rendering to the
Goldmark Markdown parser.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
