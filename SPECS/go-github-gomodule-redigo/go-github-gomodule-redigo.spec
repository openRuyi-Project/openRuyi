# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           redigo
%define go_import_path  github.com/gomodule/redigo
# Test failure due to network connection part
%define go_test_ignore_failure 1

Name:           go-github-gomodule-redigo
Version:        1.9.3
Release:        %autorelease
Summary:        Go client for Redis
License:        Apache-2.0
URL:            https://github.com/gomodule/redigo
#!RemoteAsset
Source0:        https://github.com/gomodule/redigo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/gomodule/redigo) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Redigo is a Go client for the Redis / Valkey database.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
