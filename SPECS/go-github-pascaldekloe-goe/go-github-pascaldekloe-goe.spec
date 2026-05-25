# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goe
%define go_import_path  github.com/pascaldekloe/goe

Name:           go-github-pascaldekloe-goe
Version:        0.1.1
Release:        %autorelease
Summary:        enterprise tooling
License:        CC0-1.0
URL:            https://github.com/pascaldekloe/goe
#!RemoteAsset:  sha256:bc621f0d890acea58393d69b8e5b2558bcd8ccadf940b309157c876a3304228f
Source0:        https://github.com/pascaldekloe/goe/archive/refs/tags/v0.1.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-fix-non-constant-differ-format.patch

BuildOption(prep):  -n goe-0.1.1

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pascaldekloe/goe) = %{version}
Provides:       go(github.com/pascaldekloe/goe/el) = %{version}
Provides:       go(github.com/pascaldekloe/goe/metrics) = %{version}
Provides:       go(github.com/pascaldekloe/goe/rest) = %{version}
Provides:       go(github.com/pascaldekloe/goe/verify) = %{version}


%description
Go Enterprise

Common enterprise features for the Go programming language.

This is free and unencumbered software released into the public domain
(http://creativecommons.org/publicdomain/zero/1.0).

[Image: Build Status]
(https://github.com/pascaldekloe/goe/actions/workflows/go.yml/badge.svg)
(https://github.com/pascaldekloe/goe/actions/workflows/go.yml)


%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
