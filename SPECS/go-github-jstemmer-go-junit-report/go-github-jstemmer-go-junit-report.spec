# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-junit-report
%define go_import_path  github.com/jstemmer/go-junit-report

Name:           go-github-jstemmer-go-junit-report
Version:        1.0.0
Release:        %autorelease
Summary:        Go test output to JUnit XML converter
License:        MIT
URL:            https://github.com/jstemmer/go-junit-report
#!RemoteAsset:  sha256:a44cdb1b4741b0d6bcd2390374594a29b6dc8767f56de43a09be9eec08d1707d
Source0:        https://github.com/jstemmer/go-junit-report/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/jstemmer/go-junit-report) = %{version}

%description
go-junit-report converts go test output to JUnit XML.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
