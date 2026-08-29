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
Summary:        Enterprise tooling for Go
License:        CC0-1.0
URL:            https://github.com/pascaldekloe/goe
#!RemoteAsset:  sha256:bc621f0d890acea58393d69b8e5b2558bcd8ccadf940b309157c876a3304228f
Source0:        https://github.com/pascaldekloe/goe/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
# Current Go vet rejects non-constant format strings passed to differ; keep
# tests enabled but disable vet instead of patching upstream source.
# - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pascaldekloe/goe) = %{version}

%description
goe provides common enterprise helpers for Go programs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
