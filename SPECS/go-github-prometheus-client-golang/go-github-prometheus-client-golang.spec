# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           client_golang
%define go_import_path  github.com/prometheus/client_golang
# These are sample code, so no need for testing - 251
%define go_test_exclude_glob %{shrink:
    github.com/prometheus/client_golang/tutorials*
    github.com/prometheus/client_golang/examples*
}

Name:           go-github-prometheus-client-golang
Version:        1.23.2
Release:        %autorelease
Summary:        Prometheus instrumentation library for Go applications
License:        Apache-2.0
URL:            https://github.com/prometheus/client_golang
#!RemoteAsset
Source0:        https://github.com/prometheus/client_golang/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-github-prometheus-client-golang/1.23.2-1/debian/patches/0005-Disable-tests-that-break-with-golang-1.25.patch
Patch0:         2000-Fix-collector-metrics-test-for-Go-1.25.patch
Patch1:         2001-skip-mutiple-tests.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/prometheus/client_golang) = %{version}

Requires:       go(github.com/beorn7/perks)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/kylelemons/godebug)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(go.uber.org/goleak)
Requires:       go(google.golang.org/protobuf)

%description
This is the Go (http://golang.org) client library for Prometheus
(http://prometheus.io). It has two separate parts, one for instrumenting
application code, and one for creating clients that talk to the
Prometheus HTTP API.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
