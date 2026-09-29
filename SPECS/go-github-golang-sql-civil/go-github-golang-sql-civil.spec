# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           civil
%define go_import_path  github.com/golang-sql/civil

Name:           go-github-golang-sql-civil
Version:        0+git20190719.cb61b32
Release:        %autorelease
Summary:        Go library for civil
License:        Apache-2.0
URL:            https://github.com/golang-sql/civil
VCS:            git:https://github.com/golang-sql/civil.git
#!RemoteAsset:  sha256:fe088ec5d296bfc7f152eb16d5a069526973f6f1f079fdde5ba70e3c3443d25e
Source0:        https://github.com/golang-sql/civil/archive/cb61b32ac6fe.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n civil-cb61b32ac6fe84d34b81730175f91965e43d0f90

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golang-sql/civil) = %{version}

%description
This package provides the github.com/golang-sql/civil Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
