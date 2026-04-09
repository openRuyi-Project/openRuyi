# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datadriven
%define go_import_path  github.com/cockroachdb/datadriven

Name:           go-github-cockroachdb-datadriven
Version:        1.0.2
Release:        %autorelease
Summary:        Data-Driven Testing for Go
License:        Apache-2.0
URL:            https://github.com/cockroachdb/datadriven
#!RemoteAsset
Source0:        https://github.com/cockroachdb/datadriven/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pmezard/go-difflib)

Provides:       go(github.com/cockroachdb/datadriven) = %{version}

%description
Data-Driven Tests for Go

This repository implements an extension of Table-Driven Testing
(https://github.com/golang/go/wiki/TableDrivenTests). Instead of
building and iterating over a table in the test code, the input is
further separated into files (or inline strings). For certain classes of
tests, this can significantly reduce the friction involved in writing
and reading these tests.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
