# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ristretto
%define go_import_path  github.com/dgraph-io/ristretto/v2

Name:           go-github-dgraph-io-ristretto-v2
Version:        2.4.2
Release:        %autorelease
Summary:        High-performance concurrent cache for Go
License:        Apache-2.0
URL:            https://github.com/dgraph-io/ristretto
#!RemoteAsset:  sha256:e1b63f53f6b29ccc27d6aca93e323cd9b20a7375301e83d642ce9f187424660c
Source0:        https://github.com/dgraph-io/ristretto/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dgryski/go-farm)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(golang.org/x/sys)

%description
Ristretto is a fast, concurrent, fixed-size in-memory cache optimized for
high throughput and a high cache hit ratio.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
