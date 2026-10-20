# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pester
%define go_import_path  github.com/sethgrid/pester

# The first completed worker stops its peers, so the total attempt count varies.
# Skip flaky retry-count assertions: TestConcurrentRequests[With429] reports
# "got 7 attempts, want 9"; TestMaxRetriesConcurrentRequestsWith429 reports
# "got 14 attempts, want 15".
%global go_test_flags_default -v -skip '^Test(ConcurrentRequests(With429)?|MaxRetriesConcurrentRequestsWith429)$'

Name:           go-github-sethgrid-pester
Version:        1.2.0
Release:        %autorelease
Summary:        Resilient HTTP client for Go
License:        MIT
URL:            https://github.com/sethgrid/pester
#!RemoteAsset:  sha256:7d573b79135a019e3c1cfc013784937e6015e17a66a20e39ce131196de112b79
Source0:        https://github.com/sethgrid/pester/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/sethgrid/pester) = %{version}

%description
Pester wraps the standard Go HTTP client with configurable retries, concurrency,
and backoff strategies.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
