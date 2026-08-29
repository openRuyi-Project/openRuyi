# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           treemap
%define go_import_path  github.com/igrmk/treemap/v2
# The tagged archive stores the Go module in v2/; enter that directory to
# avoid installing and testing it as github.com/igrmk/treemap/v2/v2.
%define go_test_include %{go_import_path}

Name:           go-github-igrmk-treemap-v2
Version:        2.0.1
Release:        %autorelease
Summary:        Generic sorted map for Go with red-black tree under the hood
License:        Unlicense
URL:            https://github.com/igrmk/treemap
#!RemoteAsset:  sha256:65650b8b7d828eef81ab37dfd9991a66e3f11d67355772e39fbb8fe8d2a8decf
Source0:        https://github.com/igrmk/treemap/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}/v2

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/igrmk/treemap/v2) = %{version}

%description
TreeMap is a generic key-sorted map using a red-black tree under the
hood.
It requires and relies on Go 1.18 (https://tip.golang.org/doc/go1.18)
generics feature. Iterators are designed after C++.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
