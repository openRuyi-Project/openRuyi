# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ws
%define go_import_path  github.com/gobwas/ws

Name:           go-github-gobwas-ws
Version:        1.4.0
Release:        %autorelease
Summary:        Tiny WebSocket library for Go.
License:        MIT
URL:            https://github.com/gobwas/ws
#!RemoteAsset
Source0:        https://github.com/gobwas/ws/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gobwas/httphead)
BuildRequires:  go(github.com/gobwas/pool)

Provides:       go(github.com/gobwas/ws) = %{version}

%description
RFC6455 WebSocket implementation in Go.

Features

 * Zero-copy upgrade
 * No intermediate allocations during I/O
 * Low-level API which allows to build your own logic of packet handling
   and
   buffers reuse
 * High-level wrappers and helpers around API in wsutil package, which
   allow
   to start fast without digging the protocol internals

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
