# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           telemetry
%define go_import_path  golang.org/x/telemetry
%define commit_id       6cd571d43fbb06cf3ea6659089f7152e2734f215

Name:           go-golang-x-telemetry
Version:        0+git20261022.6cd571d
Release:        %autorelease
Summary:        Go toolchain telemetry collection and analysis
License:        BSD-3-Clause
URL:            https://github.com/golang/telemetry
#!RemoteAsset:  sha256:3bafbc96ee78686a6cd7b7efec7d97466cdd2fdb692a47201a139c6938d5fbba
Source0:        https://github.com/golang/telemetry/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n telemetry-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go)
BuildRequires:  go(cloud.google.com/go/cloudtasks)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/storage)
BuildRequires:  go(github.com/evanw/esbuild)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/yuin/goldmark)
BuildRequires:  go(github.com/yuin/goldmark-meta)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(golang.org/x/telemetry) = %{version}
Provides:       go(golang.org/x/telemetry/cmd/gotelemetry) = %{version}
Provides:       go(golang.org/x/telemetry/cmd/gotelemetry/internal/browser) = %{version}
Provides:       go(golang.org/x/telemetry/cmd/gotelemetry/internal/csv) = %{version}
Provides:       go(golang.org/x/telemetry/cmd/gotelemetry/internal/view) = %{version}
Provides:       go(golang.org/x/telemetry/cmd/stacks) = %{version}
Provides:       go(golang.org/x/telemetry/config) = %{version}
Provides:       go(golang.org/x/telemetry/counter) = %{version}
Provides:       go(golang.org/x/telemetry/counter/countertest) = %{version}
Provides:       go(golang.org/x/telemetry/crashmonitor) = %{version}
Provides:       go(golang.org/x/telemetry/godev) = %{version}
Provides:       go(golang.org/x/telemetry/godev/cmd/telemetrygodev) = %{version}
Provides:       go(golang.org/x/telemetry/godev/cmd/worker) = %{version}
Provides:       go(golang.org/x/telemetry/godev/devtools/cmd/copyuploads) = %{version}
Provides:       go(golang.org/x/telemetry/godev/devtools/cmd/esbuild) = %{version}
Provides:       go(golang.org/x/telemetry/godev/internal/config) = %{version}
Provides:       go(golang.org/x/telemetry/godev/internal/content) = %{version}
Provides:       go(golang.org/x/telemetry/godev/internal/log) = %{version}
Provides:       go(golang.org/x/telemetry/godev/internal/middleware) = %{version}
Provides:       go(golang.org/x/telemetry/godev/internal/storage) = %{version}
Provides:       go(golang.org/x/telemetry/internal/browser) = %{version}
Provides:       go(golang.org/x/telemetry/internal/chartconfig) = %{version}
Provides:       go(golang.org/x/telemetry/internal/config) = %{version}
Provides:       go(golang.org/x/telemetry/internal/configgen) = %{version}
Provides:       go(golang.org/x/telemetry/internal/configstore) = %{version}
Provides:       go(golang.org/x/telemetry/internal/configtest) = %{version}
Provides:       go(golang.org/x/telemetry/internal/content) = %{version}
Provides:       go(golang.org/x/telemetry/internal/counter) = %{version}
Provides:       go(golang.org/x/telemetry/internal/crashmonitor) = %{version}
Provides:       go(golang.org/x/telemetry/internal/mmap) = %{version}
Provides:       go(golang.org/x/telemetry/internal/proxy) = %{version}
Provides:       go(golang.org/x/telemetry/internal/regtest) = %{version}
Provides:       go(golang.org/x/telemetry/internal/telemetry) = %{version}
Provides:       go(golang.org/x/telemetry/internal/testenv) = %{version}
Provides:       go(golang.org/x/telemetry/internal/unionfs) = %{version}
Provides:       go(golang.org/x/telemetry/internal/upload) = %{version}

Requires:       go(cloud.google.com/go)
Requires:       go(cloud.google.com/go/cloudtasks)
Requires:       go(cloud.google.com/go/storage)
Requires:       go(github.com/evanw/esbuild)
Requires:       go(github.com/yuin/goldmark)
Requires:       go(github.com/yuin/goldmark-meta)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/api)

%description
Go toolchain telemetry collection and analysis.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
