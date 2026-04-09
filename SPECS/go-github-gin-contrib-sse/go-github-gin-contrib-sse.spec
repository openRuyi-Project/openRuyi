# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sse
%define go_import_path  github.com/gin-contrib/sse

Name:           go-github-gin-contrib-sse
Version:        1.1.0
Release:        %autorelease
Summary:        Server-Sent Events implementation in Go. Used by the Gin Framework.
License:        MIT
URL:            https://github.com/gin-contrib/sse
#!RemoteAsset
Source0:        https://github.com/gin-contrib/sse/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/gin-contrib/sse) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Server-sent events (SSE) is a technology where a browser receives
automatic updates from a server via HTTP connection. The Server-Sent
Events EventSource API is standardized as part of HTML5 by the W3C
(http://www.w3.org/TR/2009/WD-eventsource-20091029/).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
