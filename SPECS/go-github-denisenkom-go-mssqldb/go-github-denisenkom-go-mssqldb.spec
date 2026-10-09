# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-mssqldb
%define go_import_path  github.com/denisenkom/go-mssqldb

Name:           go-github-denisenkom-go-mssqldb
Version:        0+git20191001.cfbb681
Release:        %autorelease
Summary:        Go library for go-mssqldb
License:        BSD-3-Clause
URL:            https://github.com/denisenkom/go-mssqldb
VCS:            git:https://github.com/denisenkom/go-mssqldb.git
#!RemoteAsset:  sha256:ae3dd5c142eaf3379e906e43fd94ed263a6efde66a6d625d9fd66f5d3b9d2b0e
Source0:        https://github.com/denisenkom/go-mssqldb/archive/cfbb681360f0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-mssqldb-cfbb681360f0a7de54ae77703318f0e60d422e00
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang-sql/civil)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/denisenkom/go-mssqldb) = %{version}

Requires:       go(github.com/golang-sql/civil)
Requires:       go(golang.org/x/crypto)

%description
This package provides the github.com/denisenkom/go-mssqldb Go module source.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
