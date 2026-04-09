# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           websocket
%define go_import_path  github.com/gorilla/websocket

Name:           go-github-gorilla-websocket
Version:        1.5.3
Release:        %autorelease
Summary:        Package gorilla/websocket is a fast, well-tested and widely used WebSocket implementation for Go.
License:        BSD-2-Clause
URL:            https://github.com/gorilla/websocket
#!RemoteAsset
Source0:        https://github.com/gorilla/websocket/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/gorilla/websocket) = %{version}

Requires:       go(golang.org/x/net)

%description
Gorilla WebSocket is a Go (http://golang.org/) implementation of the
WebSocket (http://www.rfc-editor.org/rfc/rfc6455.txt) protocol.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
