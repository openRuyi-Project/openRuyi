# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpmock
%define go_import_path  github.com/jarcoal/httpmock

Name:           go-github-jarcoal-httpmock
Version:        1.4.1
Release:        %autorelease
Summary:        HTTP mocking for Golang
License:        MIT
URL:            https://github.com/jarcoal/httpmock
#!RemoteAsset:  sha256:e3a047ce5ce64a49b32e5686404ce919b17eb52c4f79f3fe2faddf3701b3fec5
Source0:        https://github.com/jarcoal/httpmock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/maxatome/go-testdeep)

Provides:       go(github.com/jarcoal/httpmock) = %{version}

Requires:       go(github.com/maxatome/go-testdeep)

%description
Httpmock provides helpers for mocking HTTP responses in Go tests, allowing
clients to be tested without reaching external services.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
