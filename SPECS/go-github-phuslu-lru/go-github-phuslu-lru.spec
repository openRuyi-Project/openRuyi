# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lru
%define go_import_path  github.com/phuslu/lru

Name:           go-github-phuslu-lru
Version:        1.0.24
Release:        %autorelease
Summary:        High-performance generic LRU cache for Go
License:        MIT
URL:            https://github.com/phuslu/lru
#!RemoteAsset:  sha256:698ce233335fa595806a546b3da295c4c41083c774ee86ea6efd7e61c0eb3968
Source0:        https://github.com/phuslu/lru/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides generic LRU and TTL caches optimized for low allocation
overhead and concurrent access.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
