# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           freecache
%define go_import_path  github.com/coocood/freecache

Name:           go-github-coocood-freecache
Version:        1.2.7
Release:        %autorelease
Summary:        Cache library with zero garbage collector overhead
License:        MIT
URL:            https://github.com/coocood/freecache
#!RemoteAsset:  sha256:c8ce60c58e857735b781a4f1560b7fefd45fc84146481ab183ac01c8cfdce2c6
Source0:        https://github.com/coocood/freecache/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)

%description
FreeCache is an in-memory cache for Go that stores large numbers of entries
with zero garbage collector overhead.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
