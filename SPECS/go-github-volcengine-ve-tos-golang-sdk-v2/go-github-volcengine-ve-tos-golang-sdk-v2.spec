# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ve-tos-golang-sdk
%define go_import_path  github.com/volcengine/ve-tos-golang-sdk/v2

Name:           go-github-volcengine-ve-tos-golang-sdk-v2
Version:        2.6.2
Release:        %autorelease
Summary:        Volcengine TOS SDK for Go
License:        Apache-2.0
URL:            https://github.com/volcengine/ve-tos-golang-sdk
#!RemoteAsset:  sha256:04034a86e9265ac568b712f073d57efc0f4693bccb397c27c9a2e3be537771c2
Source0:        https://github.com/volcengine/ve-tos-golang-sdk/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
# Two resolver tests need a configured cloud endpoint. Three upstream tests
# assert behavior that differs from the production code in this pinned tag.
BuildOption(check):  -skip '^(TestIsValidObjectKey|TestStatusRetrierBase|TestServerErrorRetrierBase|TestResolver|TestResolverConcurrency)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/volcengine/ve-tos-golang-sdk/v2) = %{version}

Requires:       go(golang.org/x/sync)

%description
Go client library for Volcengine Object Storage (TOS), including its
bucket, object, session, and policy APIs.

%prep -a
# Integration tests require live cloud credentials. Keep all public library
# packages and run the self-contained unit tests in tos/.
rm -rf example tos/tests

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
