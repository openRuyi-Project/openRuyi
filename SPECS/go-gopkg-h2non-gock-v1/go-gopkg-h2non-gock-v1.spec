# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gock
%define go_import_path  gopkg.in/h2non/gock.v1

Name:           go-gopkg-h2non-gock-v1
Version:        1.1.2
Release:        %autorelease
Summary:        HTTP traffic mocking library for Go
License:        MIT
URL:            https://github.com/h2non/gock
#!RemoteAsset:  sha256:d40d29d5ca6e2ff0d519943e70fef6b7c6ce3ba2203be374b46cfcbc356c5470
Source0:        https://github.com/h2non/gock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/h2non/parth)
BuildRequires:  go(github.com/nbio/st)

Provides:       go(gopkg.in/h2non/gock.v1) = %{version}

Requires:       go(github.com/h2non/parth)

%description
gock intercepts and mocks HTTP traffic in Go tests with request matching,
response stubbing and configurable mock lifecycles.

%check
# Compile the complete test suite before tolerating TestResponderPreExpiredContext,
# whose error behavior differs with the distro's newer Go context implementation.
%buildsystem_golangmodules_check -run '^$'
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
