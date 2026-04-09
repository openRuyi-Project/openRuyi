# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           levenshtein
%define go_import_path  github.com/agext/levenshtein

Name:           go-github-agext-levenshtein
Version:        1.2.3
Release:        %autorelease
Summary:        Levenshtein distance and similarity metrics with customizable edit costs and Winkler-like bonus for common prefix.
License:        Apache-2.0
URL:            https://github.com/agext/levenshtein
#!RemoteAsset
Source0:        https://github.com/agext/levenshtein/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/agext/levenshtein) = %{version}

%description
A Go package for calculating the Levenshtein distance between two
strings

This package implements distance and similarity metrics for strings,
based on the Levenshtein measure, in Go (http://golang.org).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
