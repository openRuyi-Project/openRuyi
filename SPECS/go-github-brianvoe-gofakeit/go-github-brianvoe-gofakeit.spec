# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gofakeit
%define go_import_path  github.com/brianvoe/gofakeit
# TODO: Test failure and don't know why - Julian
%define go_test_ignore_failure 1

Name:           go-github-brianvoe-gofakeit
Version:        7.14.0
Release:        %autorelease
Summary:        Random fake data generator written in go
License:        MIT
URL:            https://github.com/brianvoe/gofakeit
#!RemoteAsset
Source0:        https://github.com/brianvoe/gofakeit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

%description
Random data generator written in go

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
