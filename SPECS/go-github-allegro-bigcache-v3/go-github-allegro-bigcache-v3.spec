# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bigcache
%define go_import_path  github.com/allegro/bigcache/v3

Name:           go-github-allegro-bigcache-v3
Version:        3.2.0
Release:        %autorelease
Summary:        Efficient cache for large numbers of Go entries
License:        Apache-2.0
URL:            https://github.com/allegro/bigcache
#!RemoteAsset:  sha256:4fc24187d81a530f2f08b34fcc7232a0ad660492a720536b1a5e1ed5557f568f
Source0:        https://github.com/allegro/bigcache/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The server stats test uses a shared cache and is not safe to run in parallel.
Patch2000:      2000-serialize-stats-index-test.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
BigCache is a fast, concurrent, eviction-based in-memory cache designed for
large numbers of entries while limiting garbage collector overhead.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
