# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-elasticsearch
%define go_import_path  github.com/elastic/go-elasticsearch/v7
# Integration tests need a live Elasticsearch cluster.
%define go_test_ignore_failure 1

Name:           go-github-elastic-go-elasticsearch-v7
Version:        7.17.10
Release:        %autorelease
Summary:        Official Go client for Elasticsearch 7.x
License:        Apache-2.0
URL:            https://github.com/elastic/go-elasticsearch
#!RemoteAsset:  sha256:85f19702bd3ee29abfdeabb53875c761cfefa6b917ff1c519da2fe4c10752d0b
Source0:        https://github.com/elastic/go-elasticsearch/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/elastic/go-elasticsearch/v7) = %{version}

%description
go-elasticsearch/v7 is the official Go client for Elasticsearch 7.x.
MinIO uses it as an event notification target.

%prep -a
# _examples are sample programs, not the library.
rm -rf _examples

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
