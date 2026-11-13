# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           util
%define go_import_path  vbom.ml/util
%define commit_id       db5cfe13f5cc80a4990d98e2e1b0707a4d1a5394

# rope tests require bruth/assert, whose source and upstream parent provide no license.
%define go_test_exclude_glob vbom.ml/util/rope

Name:           go-vbom-util
Version:        0+git20260922.db5cfe1
Release:        %autorelease
Summary:        General-purpose Go utilities with natural sorting
License:        MIT
URL:            https://github.com/fvbommel/util
#!RemoteAsset:  sha256:078d57bdfa1019fc67a71a333f28d252355f553fed0cf5334bc7bc38005eb9b5
Source0:        https://github.com/fvbommel/util/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Legacy natural-sort benchmark code converts integer code points to strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/xlab/handysort)

Provides:       go(vbom.ml/util) = %{version}

%description
This library provides natural string sorting, rope data structures and
other small utilities under the legacy vbom.ml import path.

%check -a
# Preserve compilation coverage for the public package excluded above.
go build %{go_import_path}/rope

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
