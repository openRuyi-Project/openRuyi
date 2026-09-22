# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mymysql
%define go_import_path  github.com/ziutek/mymysql
%define go_test_include %{shrink:
    %{go_import_path}/autorc
    %{go_import_path}/godrv
    %{go_import_path}/mysql
    %{go_import_path}/native
    %{go_import_path}/thrsafe
}

Name:           go-github-ziutek-mymysql
Version:        1.5.4
Release:        %autorelease
Summary:        Pure Go MySQL client and database/sql driver
License:        BSD-3-Clause
URL:            https://github.com/ziutek/mymysql
VCS:            git:https://github.com/ziutek/mymysql.git
#!RemoteAsset:  sha256:111b478d6190786ee098af3f365be0e33ed59e30ec4a2a9066b714515089f062
Source0:        https://github.com/ziutek/mymysql/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Runtime tests require a configured MySQL server. Compile the packages and
# tests in the isolated build root without attempting a database connection.
BuildOption(check):  -vet=off -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/ziutek/mymysql) = %{version}

%description
MyMySQL is a pure Go implementation of the MySQL client protocol. It includes
native and thread-safe engines and a database/sql driver.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
