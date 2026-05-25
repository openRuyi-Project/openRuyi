# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpcache
%define go_import_path  github.com/gregjones/httpcache
%define commit_id 901d90724c7919163f472a9812253fb26761123d

Name:           go-github-gregjones-httpcache
Version:        0+git20260607.901d907
Release:        %autorelease
Summary:        HTTP caching transport for Go
License:        MIT
URL:            https://github.com/gregjones/httpcache
#!RemoteAsset:  sha256:a376d4c6c17fdf7659b3952dbba20295563b767d79b6aab2fbac94c00cee0bf2
Source0:        https://github.com/gregjones/httpcache/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bradfitz/gomemcache/memcache)
BuildRequires:  go(github.com/gomodule/redigo)
BuildRequires:  go(github.com/peterbourgon/diskv)
BuildRequires:  go(github.com/syndtr/goleveldb)

Provides:       go(github.com/gregjones/httpcache) = %{version}

Requires:       go(github.com/bradfitz/gomemcache/memcache)
Requires:       go(github.com/gomodule/redigo)
Requires:       go(github.com/peterbourgon/diskv)
Requires:       go(github.com/syndtr/goleveldb)

%description
This package provides an HTTP caching transport for Go.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
