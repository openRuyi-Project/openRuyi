# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           generics
%define go_import_path  github.com/jesseduffield/generics
%define commit_id       b0b4a53a6f5ce0dc20c8a38a4e4b56e366494159
# TestMapToSlice asserts a Go map iteration order, which is unspecified and
# fails on some OBS workers.
%define go_test_ignore_failure 1

Name:           go-github-jesseduffield-generics
Version:        0+git20260621.b0b4a53
Release:        %autorelease
Summary:        extensions on the official Go generics packages
License:        MIT
URL:            https://github.com/jesseduffield/generics
#!RemoteAsset:  sha256:a32bb66eb06fcb65b3a056ebb494f90c7be07cfa3482d9ea1e54e3ada5490468
Source0:        https://github.com/jesseduffield/generics/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/wk8/go-ordered-map/v2)
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/jesseduffield/generics) = %{version}

Requires:       go(github.com/wk8/go-ordered-map/v2)
Requires:       go(golang.org/x/exp)

%description
generics is a small Go library of generic slice and map helper functions.

# slices/ and list/ use an older x/exp slices API (bool comparator) that no
# longer compiles; downstream (lazygit) only uses maps/set/orderedset.
%prep -a
rm -rf slices list

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
