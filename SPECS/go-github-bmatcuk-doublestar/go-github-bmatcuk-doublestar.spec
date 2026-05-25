# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           doublestar
%define go_import_path  github.com/bmatcuk/doublestar
# TestMatch has a path.Match("a[", "a") case incompatible with Go 1.25's
# stricter bad-pattern handling. examples/find.go imports
# github.com/bmatcuk/doublestar/v2, which is not provided by this v1 module
# package - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}
    %{go_import_path}/examples*
}

Name:           go-github-bmatcuk-doublestar
Version:        1.3.4
Release:        %autorelease
Summary:        Implements support for double star (**) matches
License:        MIT
URL:            https://github.com/bmatcuk/doublestar
#!RemoteAsset:  sha256:955fc82b044496894749edda9ca88390b478c59a8d01d23d9c38b8506864eabe
Source0:        https://github.com/bmatcuk/doublestar/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bmatcuk/doublestar) = %{version}

%description
Path pattern matching and globbing supporting doublestar (**) patterns.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
