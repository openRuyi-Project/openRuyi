# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-conntrack
%define go_import_path  github.com/mwitkow/go-conntrack
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id 2f068394615f73e460c2f3d2c158b0ad9321cadb
# circular dependency with github.com/prometheus/client_golang
%define go_test_ignore_failure 1

Name:           go-github-mwitkow-go-conntrack
Version:        0+git20260108.2f06839
Release:        %autorelease
Summary:        Go middleware for net.Conn tracking (Prometheus/trace)
License:        Apache-2.0
URL:            https://github.com/mwitkow/go-conntrack
#!RemoteAsset
Source0:        https://github.com/mwitkow/go-conntrack/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/jpillora/backoff)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/mwitkow/go-conntrack) = %{version}

Requires:       go(github.com/jpillora/backoff)
Requires:       go(golang.org/x/net)

%description
Go tracing and monitoring (Prometheus) for net.Conn

Prometheus (https://prometheus.io/) monitoring and x/net/trace
(https://godoc.org/golang.org/x/net/trace#EventLog) tracing wrappers
net.Conn, both inbound (net.Listener) and outbound (net.Dialer).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
