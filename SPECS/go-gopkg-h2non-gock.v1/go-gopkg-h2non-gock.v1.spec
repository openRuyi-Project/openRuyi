# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gock
%define go_import_path  gopkg.in/h2non/gock.v1

Name:           go-gopkg-h2non-gock.v1
Version:        1.2.0
Release:        %autorelease
Summary:        HTTP traffic mocking and testing for Go
License:        MIT
URL:            https://github.com/h2non/gock
#!RemoteAsset:  sha256:0db31a91f50714066a40ae4d9ab1b488d10e3475235579564d9156c1a7559417
Source0:        https://github.com/h2non/gock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Avoid relying on sub-millisecond scheduler timing in the context test.
Patch1:         2000-tests-make-pre-expired-context-deterministic.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/h2non/parth)
BuildRequires:  go(github.com/nbio/st)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/h2non/parth)

%description
Gock intercepts and matches HTTP requests to provide deterministic mocked
responses in Go tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
