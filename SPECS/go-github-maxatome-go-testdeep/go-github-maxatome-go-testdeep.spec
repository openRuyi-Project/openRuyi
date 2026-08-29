# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-testdeep
%define go_import_path  github.com/maxatome/go-testdeep

Name:           go-github-maxatome-go-testdeep
Version:        1.15.0
Release:        %autorelease
Summary:        Flexible deep comparison helpers for Go tests
License:        BSD-2-Clause
URL:            https://github.com/maxatome/go-testdeep
#!RemoteAsset:  sha256:ddc106b33e174f01e6536ea2a3c949547b95c28837749b5e62b53f7e01026269
Source0:        https://github.com/maxatome/go-testdeep/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/maxatome/go-testdeep) = %{version}

%description
go-testdeep provides flexible deep comparison operators and helpers for
writing Go tests.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
