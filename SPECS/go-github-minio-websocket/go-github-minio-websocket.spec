# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           websocket
%define go_import_path  github.com/minio/websocket

Name:           go-github-minio-websocket
Version:        1.6.0
Release:        %autorelease
Summary:        A fast, well-tested and widely used WebSocket implementation for Go.
License:        BSD-2-Clause
URL:            https://github.com/minio/websocket
#!RemoteAsset
Source0:        https://github.com/minio/websocket/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/minio/websocket) = %{version}

%description
The Gorilla WebSocket package provides a complete and tested
implementation of the WebSocket (http://www.rfc-
editor.org/rfc/rfc6455.txt) protocol. The package API is stable.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
