# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gorp.v1
%define go_import_path  gopkg.in/gorp.v1

Name:           go-gopkg-gorp-v1
Version:        1.7.2
Release:        %autorelease
Summary:        Provides a simple way to marshal Go structs to and from SQL databases
License:        MIT
URL:            https://github.com/go-gorp/gorp
VCS:            git:https://github.com/go-gorp/gorp.git
#!RemoteAsset:  sha256:63488c583d4bf25eb03f8224eef5934158da81650063a96b53ff4f50b9ff5409
Source0:        https://github.com/go-gorp/gorp/archive/v1.7.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gorp-1.7.2
BuildOption(check):  -vet=off -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/ziutek/mymysql)

Provides:       go(gopkg.in/gorp.v1) = %{version}

%description
This package provides the gopkg.in/gorp.v1 Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
