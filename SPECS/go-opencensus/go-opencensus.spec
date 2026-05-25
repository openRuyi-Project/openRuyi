# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go.opencensus.io
%define go_import_path  go.opencensus.io
# plugin/ochttp hits https://example.com during TestAgainstSpecs, which fails
# in the OBS network sandbox.
%define go_test_exclude go.opencensus.io/plugin/ochttp

Name:           go-opencensus
Version:        0.24.0
Release:        %autorelease
Summary:        Go library for go.opencensus.io
License:        Apache-2.0
URL:            https://github.com/census-instrumentation/opencensus-go
#!RemoteAsset:  sha256:048708914541817193330ce052026deb0c617c9d953ac15ae601ab2bde5788d1
Source0:        https://github.com/census-instrumentation/opencensus-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opencensus-go-0.24.0

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc/status)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opencensus.io) = %{version}
Provides:       go(go.opencensus.io/exporter/stackdriver/propagation) = %{version}
Provides:       go(go.opencensus.io/internal) = %{version}
Provides:       go(go.opencensus.io/internal/readme) = %{version}
Provides:       go(go.opencensus.io/internal/tagencoding) = %{version}
Provides:       go(go.opencensus.io/internal/testpb) = %{version}
Provides:       go(go.opencensus.io/metric) = %{version}
Provides:       go(go.opencensus.io/metric/metricdata) = %{version}
Provides:       go(go.opencensus.io/metric/metricexport) = %{version}
Provides:       go(go.opencensus.io/metric/metricproducer) = %{version}
Provides:       go(go.opencensus.io/metric/test) = %{version}
Provides:       go(go.opencensus.io/plugin/ocgrpc) = %{version}
Provides:       go(go.opencensus.io/plugin/ochttp) = %{version}
Provides:       go(go.opencensus.io/plugin/ochttp/propagation/b3) = %{version}
Provides:       go(go.opencensus.io/plugin/ochttp/propagation/tracecontext) = %{version}
Provides:       go(go.opencensus.io/plugin/runmetrics) = %{version}
Provides:       go(go.opencensus.io/resource) = %{version}
Provides:       go(go.opencensus.io/resource/resourcekeys) = %{version}
Provides:       go(go.opencensus.io/stats) = %{version}
Provides:       go(go.opencensus.io/stats/internal) = %{version}
Provides:       go(go.opencensus.io/stats/view) = %{version}
Provides:       go(go.opencensus.io/tag) = %{version}
Provides:       go(go.opencensus.io/trace) = %{version}
Provides:       go(go.opencensus.io/trace/internal) = %{version}
Provides:       go(go.opencensus.io/trace/propagation) = %{version}
Provides:       go(go.opencensus.io/trace/tracestate) = %{version}
Provides:       go(go.opencensus.io/zpages) = %{version}
Provides:       go(go.opencensus.io/zpages/internal) = %{version}

Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library go.opencensus.io.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
