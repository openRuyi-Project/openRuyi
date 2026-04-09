# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           treemap
%define go_import_path  github.com/igrmk/treemap

Name:           go-github-igrmk-treemap
Version:        2.0.1
Release:        %autorelease
Summary:        Generic sorted map for Go with red-black tree under the hood
License:        Unlicense
URL:            https://github.com/igrmk/treemap
#!RemoteAsset
Source0:        https://github.com/igrmk/treemap/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/igrmk/treemap) = %{version}

%description
TreeMap is a generic key-sorted map using a red-black tree under the
hood.
It requires and relies on Go 1.18 (https://tip.golang.org/doc/go1.18)
generics feature. Iterators are designed after C++.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
