# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dd-trace-go
%define go_import_path  gopkg.in/DataDog/dd-trace-go.v1
# Optional contrib integrations maintain independent framework dependency matrices.
%define go_test_exclude_glob %{go_import_path}/contrib*

Name:           go-gopkg-datadog-dd-trace-go.v1
Version:        1.33.0
Release:        %autorelease
Summary:        Datadog tracing and profiling libraries for Go
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/DataDog/dd-trace-go
#!RemoteAsset:  sha256:0e0ae7ddae2468ae06204db48bd64505c59e33de961f74300385f06c4c1af701
Source0:        https://github.com/DataDog/dd-trace-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/DataDog/dd-trace-go/commit/a83fc8bb30c3337fcd624e24f546913ca0bfb538
Patch1:         1000-profiler-support-current-pprof-aggregate-api.patch
# https://github.com/DataDog/dd-trace-go/commit/fbda83b5f
Patch2:         1001-internal-log-pass-errors-as-format-arguments.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/datadog-go)
BuildRequires:  go(github.com/DataDog/gostackparse)
BuildRequires:  go(github.com/DataDog/sketches-go)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/DataDog/datadog-go)
Requires:       go(github.com/DataDog/gostackparse)
Requires:       go(github.com/DataDog/sketches-go)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/opentracing/opentracing-go)
Requires:       go(github.com/tinylib/msgp)
Requires:       go(golang.org/x/time)
Requires:       go(golang.org/x/xerrors)
Requires:       go(google.golang.org/protobuf)

%description
Dd-trace-go provides Datadog application tracing, continuous profiling, and
instrumentation libraries for Go applications using the v1 import path.

%files
%doc README.md
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
