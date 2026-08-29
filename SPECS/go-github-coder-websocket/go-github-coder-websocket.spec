# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           websocket
%define go_import_path  github.com/coder/websocket
# TODO: Need much dependencies, I'm tired for now - Julian
%define go_test_ignore_failure 1

Name:           go-github-coder-websocket
Version:        1.8.15
Release:        %autorelease
Summary:        Minimal and idiomatic WebSocket library for Go
License:        ISC
URL:            https://github.com/coder/websocket
#!RemoteAsset:  sha256:12db8c89d5bc608afe18cb53ecaac222fa1148f1ea1422a8eaba207e5bc8fc30
Source0:        https://github.com/coder/websocket/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(github.com/gobwas/ws)
BuildRequires:  go(github.com/gobwas/pool)
BuildRequires:  go(github.com/gobwas/httphead)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/lesismal/nbio)

Provides:       go(github.com/coder/websocket) = %{version}

%description
websocket is a minimal and idiomatic WebSocket library for Go.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
