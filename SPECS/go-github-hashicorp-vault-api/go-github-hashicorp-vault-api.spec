# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  github.com/hashicorp/vault/api

Name:           go-github-hashicorp-vault-api
Version:        1.23.0
Release:        %autorelease
Summary:        Go client library for HashiCorp Vault
License:        MPL-2.0
URL:            https://github.com/hashicorp/vault
#!RemoteAsset:  sha256:3c63ed5e2f7459dc1b63ef4746b202ec79244af4e7bac82c892a265f7edc0495
Source0:        https://github.com/hashicorp/vault/archive/refs/tags/api/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use credential types exported by current cloud.google.com/go/iam.
Patch2000:      2000-use-cloud-iam-credential-types.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/awsutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/parseutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/strutil)
BuildRequires:  go(github.com/hashicorp/go-sockaddr)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/jmespath/go-jmespath)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/natefinch/atomic)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/ryanuber/go-glob)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/auth/approle) = %{version}
Provides:       go(%{go_import_path}/auth/aws) = %{version}
Provides:       go(%{go_import_path}/auth/azure) = %{version}
Provides:       go(%{go_import_path}/auth/cert) = %{version}
Provides:       go(%{go_import_path}/auth/gcp) = %{version}
Provides:       go(%{go_import_path}/auth/kubernetes) = %{version}
Provides:       go(%{go_import_path}/auth/ldap) = %{version}
Provides:       go(%{go_import_path}/auth/userpass) = %{version}

Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/iam)
Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/hashicorp/errwrap)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/hashicorp/go-retryablehttp)
Requires:       go(github.com/hashicorp/go-rootcerts)
Requires:       go(github.com/hashicorp/go-secure-stdlib/awsutil)
Requires:       go(github.com/hashicorp/go-secure-stdlib/parseutil)
Requires:       go(github.com/hashicorp/go-secure-stdlib/strutil)
Requires:       go(github.com/hashicorp/go-uuid)
Requires:       go(github.com/hashicorp/hcl)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/natefinch/atomic)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/genproto)

%description
This package provides the Go client API for interacting with HashiCorp Vault.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -a api/. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
pushd api
%buildsystem_golangmodules_check
popd

%files
%doc api/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
