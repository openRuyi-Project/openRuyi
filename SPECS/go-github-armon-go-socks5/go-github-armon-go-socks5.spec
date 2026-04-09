# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-socks5
%define go_import_path  github.com/armon/go-socks5
%define commit_id e75332964ef517daa070d7c38a9466a0d687e0a5

Name:           go-github-armon-go-socks5
Version:        0+git20160902.e753329
Release:        %autorelease
Summary:        SOCKS5 server in Golang
License:        MIT
URL:            https://github.com/armon/go-socks5
#!RemoteAsset
Source0:        https://github.com/armon/go-socks5/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/armon/go-socks5) = %{version}

%description
Provides the socks5 package that implements a SOCKS5 server
(http://en.wikipedia.org/wiki/SOCKS). SOCKS (Secure Sockets) is used to
route traffic between a client and server through an intermediate proxy
layer. This can be used to bypass firewalls or NATs.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
