# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           redis
%define go_import_path  github.com/go-redis/redis
# TODO: need dependency of redis, do it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-go-redis-redis
Version:        9.18.0
Release:        %autorelease
Summary:        Redis Go client
License:        BSD-2-Clause
URL:            https://github.com/go-redis/redis
#!RemoteAsset
Source0:        https://github.com/go-redis/redis/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-redis/redis) = %{version}

%description
go-redis is the official Redis client library for
the Go programming language. It offers a straightforward
interface for interacting with Redis servers.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
