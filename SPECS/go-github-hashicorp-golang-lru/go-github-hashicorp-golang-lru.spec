# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golang-lru
%define go_import_path  github.com/hashicorp/golang-lru

Name:           go-github-hashicorp-golang-lru
Version:        2.0.7
Release:        %autorelease
Summary:        Golang LRU cache
License:        MPL-2.0
URL:            https://github.com/hashicorp/golang-lru
#!RemoteAsset
Source0:        https://github.com/hashicorp/golang-lru/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/golang-lru) = %{version}

%description
This provides the lru package which implements a fixed-size thread safe
LRU cache. It is based on the cache in Groupcache.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
