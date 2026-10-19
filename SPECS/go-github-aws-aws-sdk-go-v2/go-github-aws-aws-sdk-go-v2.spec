# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-sdk-go-v2
%define go_import_path  github.com/aws/aws-sdk-go-v2
%define upstream_version  2026-05-21
# The release archive contains generated service and benchmark packages outside
# the core module surface packaged here; testing the whole archive pulls in
# unrelated v1 SDK and private smithy test helpers.
# Keep the SDK in one package. Debian and Fedora do not split aws-sdk-go-v2, and
# the upstream release archive already contains the service submodules; splitting
# them creates file ownership conflicts and unnecessary bootstrap cycles.
# - HNO3Miracle
%define go_test_include %{shrink:
    github.com/aws/aws-sdk-go-v2
    github.com/aws/aws-sdk-go-v2/aws
    github.com/aws/aws-sdk-go-v2/aws/arn
    github.com/aws/aws-sdk-go-v2/aws/defaults
    github.com/aws/aws-sdk-go-v2/aws/middleware
    github.com/aws/aws-sdk-go-v2/aws/protocol/ec2query
    github.com/aws/aws-sdk-go-v2/aws/protocol/query
    github.com/aws/aws-sdk-go-v2/aws/protocol/restjson
    github.com/aws/aws-sdk-go-v2/aws/protocol/xml
    github.com/aws/aws-sdk-go-v2/aws/ratelimit
    github.com/aws/aws-sdk-go-v2/aws/retry
    github.com/aws/aws-sdk-go-v2/aws/retry/internal/mock
    github.com/aws/aws-sdk-go-v2/aws/signer/internal/v4
    github.com/aws/aws-sdk-go-v2/aws/signer/v4
    github.com/aws/aws-sdk-go-v2/aws/transport/http
    github.com/aws/aws-sdk-go-v2/internal/auth
    github.com/aws/aws-sdk-go-v2/internal/auth/smithy
    github.com/aws/aws-sdk-go-v2/internal/awstesting
    github.com/aws/aws-sdk-go-v2/internal/awstesting/unit
    github.com/aws/aws-sdk-go-v2/internal/awsutil
    github.com/aws/aws-sdk-go-v2/internal/context
    github.com/aws/aws-sdk-go-v2/internal/endpoints
    github.com/aws/aws-sdk-go-v2/internal/endpoints/awsrulesfn
    github.com/aws/aws-sdk-go-v2/internal/middleware
    github.com/aws/aws-sdk-go-v2/internal/protocoltest
    github.com/aws/aws-sdk-go-v2/internal/rand
    github.com/aws/aws-sdk-go-v2/internal/sdk
    github.com/aws/aws-sdk-go-v2/internal/sdkio
    github.com/aws/aws-sdk-go-v2/internal/shareddefaults
    github.com/aws/aws-sdk-go-v2/internal/strings
    github.com/aws/aws-sdk-go-v2/internal/sync/singleflight
    github.com/aws/aws-sdk-go-v2/internal/timeconv
}

Name:           go-github-aws-aws-sdk-go-v2
Version:        20260521
Release:        %autorelease
Summary:        AWS SDK for Go v2 core module
License:        Apache-2.0
URL:            https://github.com/aws/aws-sdk-go-v2
#!RemoteAsset:  sha256:68459245a574d7320592e7fd2575129de825acecfa0ab7b8f674261907c6887a
Source0:        https://github.com/aws/aws-sdk-go-v2/archive/release-%{upstream_version}.tar.gz#/%{_name}-release-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Allow hash/checksum fixtures to seek while newer Smithy computes body length.
# https://github.com/aws/aws-sdk-go-v2/commit/c5510c6fa70019f93af63e53b8fc2db59fc44996
Patch1000:      1000-tests-allow-body-length-seeks-before-hashing.patch
# Otherwise we need to -vet=off
Patch2000:      2000-Wrap-status-code-error-value-for-Go-1.27.patch
# Match the bucket-level paths produced by the system Smithy JoinPath fix.
# https://github.com/aws/smithy-go/pull/698
Patch2001:      2001-tests-expect-Smithy-bucket-trailing-slash.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/smithy-go)

Provides:       go(github.com/aws/aws-sdk-go-v2) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/config) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/credentials) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/internal/configsources) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/internal/ini) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/internal/v4a) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/dynamodb) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/ec2) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/ecs) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/elasticache) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/internal/checksum) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/internal/endpoint-discovery) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/internal/s3shared) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/kafka) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/lightsail) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/rds) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/s3) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/signin) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/sso) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/ssooidc) = %{version}
Provides:       go(github.com/aws/aws-sdk-go-v2/service/sts) = %{version}

Requires:       go(github.com/aws/smithy-go)

%description
This package provides the AWS SDK for Go v2 core module and selected service
module import paths from the upstream release archive.

%check -a
# These module trees are already installed by the aggregate package. Keep the
# existing core tests and exercise every package in the newly exposed modules.
go test -v \
    %{go_import_path}/aws/protocol/eventstream/... \
    %{go_import_path}/internal/v4a/... \
    %{go_import_path}/service/dynamodb/... \
    %{go_import_path}/service/internal/checksum/... \
    %{go_import_path}/service/internal/endpoint-discovery/... \
    %{go_import_path}/service/internal/s3shared/... \
    %{go_import_path}/service/s3/...

%files
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE.txt
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
