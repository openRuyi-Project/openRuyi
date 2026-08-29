# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stackdriver
%define go_import_path  contrib.go.opencensus.io/exporter/stackdriver
# Backport upstream cloud-go API update and direct prometheus dependency removal
# so this exporter builds against the cloud.google.com/go packages in openRuyi.
# Root package tests require Google Application Default Credentials for
# Stackdriver clients in OBS; subpackage tests still run. - HNO3Miracle
%define go_test_exclude %{go_import_path}

Name:           go-opencensus-contrib-exporter-stackdriver
Version:        0.13.14
Release:        %autorelease
Summary:        OpenCensus Stackdriver exporter for Go
License:        Apache-2.0
URL:            https://github.com/census-ecosystem/opencensus-go-exporter-stackdriver
#!RemoteAsset:  sha256:0edcd9dc950a1621d8d6757a028fa7bdad7772ddad206dd1d06d1d945e99ec65
Source0:        https://github.com/census-ecosystem/opencensus-go-exporter-stackdriver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Update old monitoringpb imports to the packaged cloud-go monitoring API,
# avoid pulling the full Prometheus source only for stale NaN helpers, and fix
# Go vet non-constant format-string failures. The stale NaN behavior is kept
# identical by copying the upstream Prometheus constants locally. - HNO3Miracle
Patch2000:      2000-update-cloud-go-api-and-drop-prometheus-dependency.patch

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/compute)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(cloud.google.com/go/trace)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/census-instrumentation/opencensus-proto)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/jmespath/go-jmespath)
BuildRequires:  go(github.com/jstemmer/go-junit-report)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rakyll/embedmd)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(golang.org/x/lint)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/appengine)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(honnef.co/go/tools)
BuildRequires:  go-rpm-macros

Provides:       go(contrib.go.opencensus.io/exporter/stackdriver) = %{version}

Requires:       go(cloud.google.com/go/compute)
Requires:       go(cloud.google.com/go/monitoring)
Requires:       go(cloud.google.com/go/trace)
Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/BurntSushi/toml)
Requires:       go(github.com/census-instrumentation/opencensus-proto)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/jmespath/go-jmespath)
Requires:       go(github.com/jstemmer/go-junit-report)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/rakyll/embedmd)
Requires:       go(go.opencensus.io)
Requires:       go(golang.org/x/lint)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/xerrors)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/appengine)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(honnef.co/go/tools)

%description
This package provides OpenCensus Stackdriver exporter for Go.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
