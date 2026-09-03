# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fuzzy-patricia.v3
%define go_import_path  gopkg.in/ozeidan/fuzzy-patricia.v3

Name:           go-gopkg-ozeidan-fuzzy-patricia-v3
Version:        3.0.0
Release:        %autorelease
Summary:        A generic patricia trie (also called radix tree) implemented in Go (Golang)
License:        MIT
URL:            https://github.com/ozeidan/fuzzy-patricia
#!RemoteAsset:  sha256:ef127cd2ece64bbd4e78efe6c305c299778e7a0175bfa861351b14ac58fbcc5c
Source0:        https://github.com/ozeidan/fuzzy-patricia/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(gopkg.in/ozeidan/fuzzy-patricia.v3) = %{version}

%description
fuzzy-patricia is a patricia-trie based fuzzy search library for Go.

%check
# Compile every package and its tests before tolerating the heap measurement.
%buildsystem_golangmodules_check -run '^$'
# TestTrie_DeleteLeakageDense compares small runtime heap deltas and is unstable
# under the OBS worker's garbage-collection and allocator environment.
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
