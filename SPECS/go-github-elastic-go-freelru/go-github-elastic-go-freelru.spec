# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-freelru
%define go_import_path  github.com/elastic/go-freelru

Name:           go-github-elastic-go-freelru
Version:        0.16.0
Release:        %autorelease
Summary:        Low-overhead generic LRU cache for Go
License:        Apache-2.0
URL:            https://github.com/elastic/go-freelru
#!RemoteAsset:  sha256:59ca0857495995909d701b00554ac39e5fb3d866c62f6ced953f5d6b258785c4
Source0:        https://github.com/elastic/go-freelru/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/allegro/bigcache/v3)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cloudflare/golibs)
BuildRequires:  go(github.com/coocood/freecache)
BuildRequires:  go(github.com/dgraph-io/ristretto/v2)
BuildRequires:  go(github.com/dolthub/maphash)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/orcaman/concurrent-map/v2)
BuildRequires:  go(github.com/phuslu/lru)
BuildRequires:  go(github.com/zeebo/xxh3)

Provides:       go(%{go_import_path}) = %{version}

%description
FreeLRU provides generic single-threaded, synchronized, and sharded LRU
caches designed to avoid garbage collector overhead.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
