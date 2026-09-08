# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fargo
%define go_import_path  github.com/hudl/fargo
# The integration suite requires a local Eureka server on port 8081.
%define go_test_exclude %{go_import_path}/tests

Name:           go-github-hudl-fargo
Version:        1.4.0
Release:        %autorelease
Summary:        Netflix Eureka client for Go
License:        MIT
URL:            https://github.com/hudl/fargo
#!RemoteAsset:  sha256:3f328d1fd2c5b9e05ff3f69c8400cf9dc7bbb14a4a57a21d2c5c8b7790238bc2
Source0:        https://github.com/hudl/fargo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use the current go-logging API; the upstream release calls the removed
# Criticalf method.
Patch2000:      2000-use-compatible-critical-logger-call.patch
# Associate the secure VIP example with the method it actually calls.
Patch2001:      2001-fix-stale-vip-example-name.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/clbanning/mxj)
BuildRequires:  go(github.com/franela/goreq)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/op/go-logging)
BuildRequires:  go(github.com/smartystreets/goconvey)
BuildRequires:  go(gopkg.in/gcfg.v1)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/clbanning/mxj)
Requires:       go(github.com/franela/goreq)
Requires:       go(github.com/miekg/dns)
Requires:       go(github.com/op/go-logging)
Requires:       go(gopkg.in/gcfg.v1)

%description
Fargo is a Go client library for Netflix Eureka service discovery.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
