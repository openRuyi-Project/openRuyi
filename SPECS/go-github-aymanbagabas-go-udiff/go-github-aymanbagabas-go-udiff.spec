# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-udiff
%define go_import_path  github.com/aymanbagabas/go-udiff

Name:           go-github-aymanbagabas-go-udiff
Version:        0.3.1
Release:        %autorelease
Summary:        µDiff - a micro Go diffing library
License:        BSD-3-Clause
URL:            https://github.com/aymanbagabas/go-udiff
#!RemoteAsset
Source0:        https://github.com/aymanbagabas/go-udiff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aymanbagabas/go-udiff) = %{version}

%description
Micro diff (µDiff) is a Go library that implements the Myers'
(http://www.xmailserver.org/diff2.pdf) diffing algorithm. It aims to
provide a minimal API to compute and apply diffs with zero dependencies.
It also supports generating diffs in the Unified Format
(https://www.gnu.org/software/diffutils/manual/html_node/Unified-
Format.html). If you are looking for a way to parse unified diffs, check
out sourcegraph/go-diff (https://github.com/sourcegraph/go-diff).

This is merely a copy of the Golang tools internal diff package
(https://github.com/golang/tools/tree/master/internal/diff) with a few
modifications to export package symbols. All credit goes to the Go
authors (https://go.dev/AUTHORS).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
