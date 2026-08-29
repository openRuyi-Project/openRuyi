# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go.opencensus.io
%define go_import_path  go.opencensus.io
# plugin/ochttp hits https://example.com during TestAgainstSpecs, which fails
# in the OBS network sandbox. plugin/ocgrpc has a timing-sensitive
# TestServerSpanDuration failure on riscv64 with "no more spans". - HNO3Miracle
%define go_test_exclude %{shrink:
    go.opencensus.io/plugin/ochttp
    go.opencensus.io/plugin/ocgrpc
}

Name:           go-opencensus
Version:        0.24.0
Release:        %autorelease
Summary:        OpenCensus library for Go
License:        Apache-2.0
URL:            https://github.com/census-instrumentation/opencensus-go
#!RemoteAsset:  sha256:048708914541817193330ce052026deb0c617c9d953ac15ae601ab2bde5788d1
Source0:        https://github.com/census-instrumentation/opencensus-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects mismatched fmt format strings in opencensus tests and
# one error path. Keep the tests enabled and fix the formats. - HNO3Miracle
Patch2000:      2000-fix-format-strings-for-go-vet.patch

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
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opencensus.io) = %{version}

Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(golang.org/x/net)
Requires:       go(google.golang.org/grpc)

%description
This package provides the Go library go.opencensus.io.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
