# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           treemap
%define go_import_path  github.com/igrmk/treemap/v2
%define commit_id c69857c24f535143274e79c5a97b79be605d4cea
# The repository keeps the v2 Go module in the v2/ subdirectory; checking only
# that module avoids testing the repository root, which intentionally has no Go files. - HNO3Miracle
%define go_test_include github.com/igrmk/treemap/v2

Name:           go-github-igrmk-treemap-v2
Version:        0+git20260607.c69857c
Release:        %autorelease
Summary:        Generic sorted map for Go with red-black tree under the hood
License:        Unlicense
URL:            https://github.com/igrmk/treemap
#!RemoteAsset:  sha256:c56f59ffe220d35566edd4217779d952140866ea3c60d6c566a5cbe0d3c751ac
Source0:        https://github.com/igrmk/treemap/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/igrmk/treemap/v2) = %{version}

Requires:       go(golang.org/x/exp)

%description
This package provides a generic ordered map implementation for Go backed by a
red-black tree.

%files
%license LICENSE
%{go_sys_gopath}/github.com/igrmk/treemap

%changelog
%autochangelog
