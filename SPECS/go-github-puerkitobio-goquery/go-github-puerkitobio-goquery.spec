# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goquery
%define go_import_path  github.com/PuerkitoBio/goquery

Name:           go-github-puerkitobio-goquery
Version:        1.12.0
Release:        %autorelease
Summary:        HTML document query and manipulation library for Go
License:        BSD-3-Clause
URL:            https://github.com/PuerkitoBio/goquery
#!RemoteAsset:  sha256:f93137d692e8fae34739b16eba5978ac3d28b2693bdffe21d3f536cc2a9e5665
Source0:        https://github.com/PuerkitoBio/goquery/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/andybalholm/cascadia)
BuildRequires:  go(golang.org/x/net)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/andybalholm/cascadia)
Requires:       go(golang.org/x/net)

%description
Goquery provides jQuery-style HTML document traversal, selection, and
manipulation using Go's HTML parser and Cascadia selectors.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
