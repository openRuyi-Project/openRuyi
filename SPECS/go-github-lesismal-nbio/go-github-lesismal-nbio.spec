# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nbio
%define go_import_path  github.com/lesismal/nbio

Name:           go-github-lesismal-nbio
Version:        1.6.8
Release:        %autorelease
Summary:        Pure Go 1000k+ connections solution, support tls/http1.x/websocket and basically compatible with net/http.
License:        MIT
URL:            https://github.com/lesismal/nbio
#!RemoteAsset
Source0:        https://github.com/lesismal/nbio/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/lesismal/llib)

Provides:       go(github.com/lesismal/nbio) = %{version}

%description
NBIO - NON-BLOCKING IO

For massive connection scenarios, combined with memory pools and
goroutine pools, it can effectively reduce the number of goroutines and
objects, thereby lowering memory consumption and GC pressure, avoiding
OOM and significant STW. For example, in a million WebSocket 1k payload
echo test, nbio can maintain memory at 1GB with 100k TPS.

For regular connection scenarios, nbio's performance is inferior to the
standard library due to goroutine affinity, lower buffer reuse rate for
individual connections, and variable escape issues.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
