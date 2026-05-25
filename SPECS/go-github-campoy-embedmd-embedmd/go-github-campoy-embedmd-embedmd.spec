# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           embedmd
%define go_import_path  github.com/campoy/embedmd
%define commit_id d497bcd9818fee20b6bdf07d9a863382a7059ae9
# The root package integration test executes the embedmd binary, which is not
# built by this library package. - HNO3Miracle
%define go_test_exclude github.com/campoy/embedmd

Name:           go-github-campoy-embedmd-embedmd
Version:        0+git20260607.d497bcd
Release:        %autorelease
Summary:        Markdown embedding library for Go
License:        Apache-2.0
URL:            https://github.com/campoy/embedmd
#!RemoteAsset:  sha256:0fc25e5c66789f7db0b4c8c47646312de031e91d9d696fe405a298652cff808c
Source0:        https://github.com/campoy/embedmd/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pmezard/go-difflib)

Provides:       go(github.com/campoy/embedmd/embedmd) = %{version}

Requires:       go(github.com/pmezard/go-difflib)

%description
This package provides the Go library used by embedmd to embed files or command
output in Markdown documents.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
