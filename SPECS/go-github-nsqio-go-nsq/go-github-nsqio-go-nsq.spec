# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-nsq
%define go_import_path  github.com/nsqio/go-nsq
# Consumer/producer tests expect a live nsqd and nsqlookupd.
%define go_test_ignore_failure 1

Name:           go-github-nsqio-go-nsq
Version:        1.1.0
Release:        %autorelease
Summary:        Official Go client for NSQ
License:        MIT
URL:            https://github.com/nsqio/go-nsq
#!RemoteAsset:  sha256:8accab4d94981d81e9d9c4067a158a7c96979c79b27917517febfc24110d5ce9
Source0:        https://github.com/nsqio/go-nsq/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/snappy)

Provides:       go(github.com/nsqio/go-nsq) = %{version}

Requires:       go(github.com/golang/snappy)

%description
go-nsq is the official Go client for NSQ, the realtime distributed
messaging platform. MinIO uses it as an event notification target.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
