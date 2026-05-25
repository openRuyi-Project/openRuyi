# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           memcache
%define go_import_path  github.com/bradfitz/gomemcache
%define commit_id 4d751bb6e37cf0da5fd57a86b880f76791307adf

Name:           go-github-bradfitz-gomemcache-memcache
Version:        0+git20260607.4d751bb
Release:        %autorelease
Summary:        Memcache client library for Go
License:        Apache-2.0
URL:            https://github.com/bradfitz/gomemcache
#!RemoteAsset:  sha256:f3d462db42a6a87739046ba9740fd9a37769b0071af27f37e4069faf4c2f1776
Source0:        https://github.com/bradfitz/gomemcache/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bradfitz/gomemcache/memcache) = %{version}

%description
This package provides a memcache client library for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
