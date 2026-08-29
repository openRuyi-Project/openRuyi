# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  google.golang.org/api
# google-api imports cloud.google.com/go/auth, while google-cloud-go-auth only
# needs the google.golang.org/api/googleapi leaf package. Keep the leaf package
# in go-google-api-support to break the bootstrap cycle without weakening tests.
# integration-tests/byoid and integration-tests/downscope require Google
# Application Default Credentials, which are not available in OBS. Auth helper
# tests in the root, idtoken, transport/grpc, and transport/http packages also
# require ADC/GCE credentials and fail with GOOGLE_APPLICATION_CREDENTIALS
# unset, "failed to create creds", or missing default credentials.
# - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}
    %{go_import_path}/idtoken
    %{go_import_path}/integration-tests/*
    %{go_import_path}/transport/grpc
    %{go_import_path}/transport/http
}

Name:           go-google-api
Version:        0.285.0
Release:        %autorelease
Summary:        Generated Google API clients for Go
License:        Apache-2.0
URL:            https://github.com/googleapis/google-api-go-client
#!RemoteAsset:  sha256:c85268bc160001abb5a439c02d4540b8475f91610d96eb014498399b841ea47f
Source0:        https://github.com/googleapis/google-api-go-client/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/emirpasic/gods)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-git/gcfg)
BuildRequires:  go(github.com/go-git/go-billy/v5)
BuildRequires:  go(github.com/go-git/go-git/v5)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-github/v59)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/jbenet/go-context)
BuildRequires:  go(github.com/kevinburke/ssh_config)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/pjbgf/sha1cd)
BuildRequires:  go(github.com/ProtonMail/go-crypto)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/skeema/knownhosts)
BuildRequires:  go(github.com/xanzy/ssh-agent)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/oauth2/google)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/warnings.v0)

Provides:       go(google.golang.org/api) = %{version}

Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/auth/oauth2adapt)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(dario.cat/mergo)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/cloudflare/circl)
Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(github.com/emirpasic/gods)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-git/gcfg)
Requires:       go(github.com/go-git/go-billy/v5)
Requires:       go(github.com/go-git/go-git/v5)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/google/go-github/v59)
Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/jbenet/go-context)
Requires:       go(github.com/kevinburke/ssh_config)
Requires:       go(github.com/klauspost/cpuid/v2)
Requires:       go(github.com/pjbgf/sha1cd)
Requires:       go(github.com/ProtonMail/go-crypto)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(github.com/skeema/knownhosts)
Requires:       go(github.com/xanzy/ssh-agent)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/oauth2/google)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/api/googleapi)
Requires:       go(google.golang.org/api/internal/third_party/uritemplates)
Requires:       go(google.golang.org/api/iterator)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/warnings.v0)

%description
google-api provides generated Go clients and support packages for Google APIs.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/googleapi
%exclude %{go_sys_gopath}/%{go_import_path}/internal/third_party/uritemplates
%exclude %{go_sys_gopath}/%{go_import_path}/iterator

%changelog
%autochangelog
