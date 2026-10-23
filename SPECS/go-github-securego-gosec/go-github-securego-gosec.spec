# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gosec
%define go_import_path  github.com/securego/gosec/v2

Name:           go-github-securego-gosec
Version:        2.29.0
Release:        %autorelease
Summary:        Holds the central scanning logic used by gosec security scanner
License:        Apache-2.0
URL:            https://github.com/securego/gosec
#!RemoteAsset:  sha256:083422c2d64f311062e7fe36ff1bd22c98b029f0a4d69f3e81fd0a4724139092
Source0:        https://github.com/securego/gosec/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go)
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/anthropics/anthropic-sdk-go)
BuildRequires:  go(github.com/bahlo/generic-list-go)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/ccojocar/zxcvbn-go)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/gookit/color)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/invopop/jsonschema)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/mozilla/tls-observatory)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/openai/openai-go/v3)
BuildRequires:  go(github.com/pb33f/ordered-map/v2)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/standard-webhooks/standard-webhooks/libraries)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/sjson)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genai)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/securego/gosec/v2) = %{version}
Provides:       go(github.com/securego/gosec/v2/analyzers) = %{version}
Provides:       go(github.com/securego/gosec/v2/autofix) = %{version}
Provides:       go(github.com/securego/gosec/v2/cmd/vflag) = %{version}
Provides:       go(github.com/securego/gosec/v2/cwe) = %{version}
Provides:       go(github.com/securego/gosec/v2/goanalysis) = %{version}
Provides:       go(github.com/securego/gosec/v2/internal/ssautil) = %{version}
Provides:       go(github.com/securego/gosec/v2/issue) = %{version}
Provides:       go(github.com/securego/gosec/v2/report) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/csv) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/golint) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/html) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/json) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/junit) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/sarif) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/sonar) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/text) = %{version}
Provides:       go(github.com/securego/gosec/v2/report/yaml) = %{version}
Provides:       go(github.com/securego/gosec/v2/rules) = %{version}
Provides:       go(github.com/securego/gosec/v2/taint) = %{version}
Provides:       go(github.com/securego/gosec/v2/testutils) = %{version}
Provides:       go(github.com/securego/gosec/v2/tools) = %{version}

Requires:       go(github.com/anthropics/anthropic-sdk-go)
Requires:       go(github.com/ccojocar/zxcvbn-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gookit/color)
Requires:       go(github.com/lib/pq)
Requires:       go(github.com/mozilla/tls-observatory)
Requires:       go(github.com/openai/openai-go/v3)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/tools)
Requires:       go(google.golang.org/genai)

%description
Holds the central scanning logic used by gosec security scanner.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n gosec-%{version}

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/github.com/securego/gosec/v2

%changelog
%autochangelog
