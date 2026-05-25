# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           groupcache
%define go_import_path  github.com/golang/groupcache

Name:           go-github-golang-groupcache
Version:        0+git20241129.2c02b82
Release:        %autorelease
Summary:        Go library for github.com/golang/groupcache
License:        Apache-2.0
URL:            https://github.com/golang/groupcache
#!RemoteAsset:  sha256:6a4d1b422304807fe23e5b6fa54036e78feede7d4db20f80da352ec19f53c1ca
Source0:        https://github.com/golang/groupcache/archive/2c02b8208cf8c02a3e358cb1d9b60950647543fc.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n groupcache-2c02b8208cf8c02a3e358cb1d9b60950647543fc

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/golang/groupcache) = %{version}
Provides:       go(github.com/golang/groupcache/lru) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library github.com/golang/groupcache.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
