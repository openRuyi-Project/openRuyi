# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           perf-utils
%define go_import_path  github.com/hodgesds/perf-utils
# These tests require tracefs, debugfs, perf_event, or CPU MSR access.
# OBS workers do not expose stable perf, tracefs, or MSR device access.
%define go_test_flags_default -v -run '^(TestCacheProfiler|TestHardwareProfiler|TestMaxOpenFiles|TestGetTids|TestSkylake)$'

Name:           go-github-hodgesds-perf-utils
Version:        0.7.0
Release:        %autorelease
Summary:        Go helpers for Linux performance counters
License:        MIT
URL:            https://github.com/hodgesds/perf-utils
#!RemoteAsset:  sha256:eb89f247f3d62695b4d70f54ea8fc59c1fab877d259e8a34a4bdf32426c64035
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/hodgesds/perf-utils) = %{version}

Requires:       go(go.uber.org/multierr)
Requires:       go(golang.org/x/sys)

%description
Go library for working with Linux performance monitoring counters.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
