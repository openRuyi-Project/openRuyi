# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golang-lru
%define go_import_path  github.com/hashicorp/golang-lru/v2

# ExampleLRU in expirable is timing-sensitive in OBS.
%define go_test_exclude github.com/hashicorp/golang-lru/v2/expirable

Name:           go-github-hashicorp-golang-lru-v2
Version:        2.0.7
Release:        %autorelease
Summary:        Golang LRU cache
License:        MPL-2.0
URL:            https://github.com/hashicorp/golang-lru
#!RemoteAsset:  sha256:312697d0bf6e6bb44e66a94b2a8a07955edf89af10b09e69b5a9101d30ad5149
Source0:        https://github.com/hashicorp/golang-lru/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/golang-lru/v2) = %{version}

%description
This provides the lru package which implements a fixed-size thread safe
LRU cache. It is based on the cache in Groupcache.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
