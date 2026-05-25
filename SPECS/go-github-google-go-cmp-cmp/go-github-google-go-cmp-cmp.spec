# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cmp
%define go_import_path  github.com/google/go-cmp
%define commit_id 34c9473539b8d7c62273a8f4acb27c0c32295330

Name:           go-github-google-go-cmp-cmp
Version:        0+git20260310.34c9473
Release:        %autorelease
Summary:        Package for comparing Go values in tests
License:        BSD-3-Clause
URL:            https://github.com/google/go-cmp
#!RemoteAsset:  sha256:53c00a86fccdd925fc0dd63c2842868dff3d585cfe39d5e5259d4ca48c5d70bb
Source0:        https://github.com/google/go-cmp/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/go-cmp/cmp) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/cmpopts) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/internal/diff) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/internal/flags) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/internal/function) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/internal/testprotos) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/internal/teststructs) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/internal/teststructs/foo1) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/internal/teststructs/foo2) = %{version}
Provides:       go(github.com/google/go-cmp/cmp/internal/value) = %{version}

%description
This package provides comparison helpers for Go values, primarily for tests.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
