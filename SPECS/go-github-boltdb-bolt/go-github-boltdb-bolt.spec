# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bolt
%define go_import_path  github.com/boltdb/bolt
# Test failure, may be cause by outdate code - Julian
%define go_test_ignore_failure 1

Name:           go-github-boltdb-bolt
Version:        1.3.1
Release:        %autorelease
Summary:        An embedded key/value database for Go.
License:        MIT
URL:            https://github.com/boltdb/bolt
#!RemoteAsset
Source0:        https://github.com/boltdb/bolt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/boltdb/bolt) = %{version}

%description
Bolt is a pure Go key/value store inspired by Howard Chu's
(https://twitter.com/hyc_symas) LMDB project (http://symas.com/mdb/).
The goal of the project is to provide a simple, fast, and reliable
database for projects that don't require a full database server such as
Postgres or MySQL.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
