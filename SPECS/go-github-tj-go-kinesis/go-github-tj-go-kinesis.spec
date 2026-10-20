# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-kinesis
%define go_import_path  github.com/tj/go-kinesis
%global commit_id       08b17f58cb1b2ace14a61c0619a6bf2e2245ccd6

Name:           go-github-tj-go-kinesis
Version:        0+git20261020.08b17f5
Release:        %autorelease
Summary:        Batched producer for Amazon Kinesis
License:        MIT
URL:            https://github.com/tj/go-kinesis
#!RemoteAsset:  sha256:ffbdb9f9d3b3b067ba0eeaeb441383b14be3a50f0f84269886db4db7a235f7bc
Source0:        https://github.com/tj/go-kinesis/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-kinesis-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apex/log)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/jpillora/backoff)

Provides:       go(github.com/tj/go-kinesis) = %{version}

Requires:       go(github.com/apex/log)
Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/jpillora/backoff)

%description
This package provides a batched Amazon Kinesis producer using the
official AWS SDK for Go.

%files
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
