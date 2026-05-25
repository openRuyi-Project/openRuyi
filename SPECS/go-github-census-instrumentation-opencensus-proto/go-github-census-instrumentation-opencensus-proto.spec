# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opencensus-proto
%define go_import_path  github.com/census-instrumentation/opencensus-proto

Name:           go-github-census-instrumentation-opencensus-proto
Version:        0.4.1
Release:        %autorelease
Summary:        OpenCensus protocol buffers for Go
License:        Apache-2.0
URL:            https://github.com/census-instrumentation/opencensus-proto
#!RemoteAsset:  sha256:e3d89f7f9ed84c9b6eee818c2e9306950519402bf803698b15c310b77ca2f0f3
Source0:        https://github.com/census-instrumentation/opencensus-proto/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/census-instrumentation/opencensus-proto) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides OpenCensus protocol buffers for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
