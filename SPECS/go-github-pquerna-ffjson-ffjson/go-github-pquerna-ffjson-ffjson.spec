# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ffjson
%define go_import_path  github.com/pquerna/ffjson
%define commit_id aa0246cd15f76c96de6b96f22a305bdfb2d1ec02
# The tests/* fixtures require generated ffjson output and github.com/google/gofuzz;
# the library packages build and test independently without those generated fixtures.
%define go_test_exclude_glob github.com/pquerna/ffjson/tests*

Name:           go-github-pquerna-ffjson-ffjson
Version:        0+git20190930.aa0246c
Release:        %autorelease
Summary:        faster JSON serialization for Go
License:        Apache-2.0
URL:            https://github.com/pquerna/ffjson
#!RemoteAsset:  sha256:a5159175a7faa006a187ce617679e689ed5951401f54de536a4237d821e8f505
Source0:        https://github.com/pquerna/ffjson/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pquerna/ffjson/ffjson) = %{version}
Provides:       go(github.com/pquerna/ffjson/fflib/v1) = %{version}


%description
ffjson: faster JSON for Go

[Image: Build Status] (https://travis-
ci.org/pquerna/ffjson.svg?branch=master) (https://travis-
ci.org/pquerna/ffjson) [Image: Fuzzit Status]
(https://app.fuzzit.dev/badge?org_id=pquerna)
(https://app.fuzzit.dev/orgs/pquerna/dashboard)

ffjson generates static MarshalJSON and UnmarshalJSON functions for
structures in Go. The generated functions reduce the reliance upon
runtime reflection to do serialization and are generally 2 to 3 times

%files
%doc README.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
