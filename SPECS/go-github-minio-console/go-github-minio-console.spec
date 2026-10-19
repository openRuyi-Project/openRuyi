# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           console
%global go_import_path  github.com/minio/console
# Integration tests need running MinIO/Console services; without them they log
# "authentication token not found in cookies response" and exit before testing.
%global go_test_exclude %{go_import_path}/integration
%global module_version v1.7.7-0.20250905210349-2017f33b26e1

Name:           go-github-minio-console
Version:        1.7.6+git20261020.2017f33
Release:        %autorelease
Summary:        MinIO Console server Go libraries and embedded web assets
License:        AGPL-3.0-or-later
URL:            https://github.com/minio/console
# Upstream GitHub repository is unavailable. The Go proxy retains this immutable
# module archive, whose Go checksum matches the MinIO release go.sum.
#!RemoteAsset:  sha256:bf83d208e34239c92c2839b92afd9bcc4b607945786ddb4a2d2319be6139790b
Source0:        https://proxy.golang.org/github.com/minio/console/@v/%{module_version}.zip#/console-%{version}.zip
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go uses a specialized error type for an invalid duration.
Patch2000:      2000-compare-duration-error-messages.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  unzip
BuildRequires:  go(github.com/blang/semver/v4)
BuildRequires:  go(github.com/cheggaaa/pb/v3)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/go-openapi/runtime)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/validate)
BuildRequires:  go(github.com/golang-jwt/jwt/v4)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/minio/cli)
BuildRequires:  go(github.com/minio/highwayhash)
BuildRequires:  go(github.com/minio/kes)
BuildRequires:  go(github.com/minio/madmin-go/v3)
BuildRequires:  go(github.com/minio/mc)
BuildRequires:  go(github.com/minio/minio-go/v7)
BuildRequires:  go(github.com/minio/pkg/v3)
BuildRequires:  go(github.com/minio/selfupdate)
BuildRequires:  go(github.com/minio/websocket)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/secure-io/sio-go)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/unrolled/secure)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)

Provides:       go(github.com/minio/console) = %{version}

Requires:       go(github.com/blang/semver/v4)
Requires:       go(github.com/cheggaaa/pb/v3)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/go-openapi/errors)
Requires:       go(github.com/go-openapi/loads)
Requires:       go(github.com/go-openapi/runtime)
Requires:       go(github.com/go-openapi/spec)
Requires:       go(github.com/go-openapi/strfmt)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/go-openapi/validate)
Requires:       go(github.com/golang-jwt/jwt/v4)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/jessevdk/go-flags)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/minio/cli)
Requires:       go(github.com/minio/highwayhash)
Requires:       go(github.com/minio/kes)
Requires:       go(github.com/minio/madmin-go/v3)
Requires:       go(github.com/minio/mc)
Requires:       go(github.com/minio/minio-go/v7)
Requires:       go(github.com/minio/pkg/v3)
Requires:       go(github.com/minio/selfupdate)
Requires:       go(github.com/minio/websocket)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/secure-io/sio-go)
Requires:       go(github.com/unrolled/secure)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)

%description
Go libraries for the MinIO web console server, including its API handlers
and the upstream embedded web application assets and their source files.

%prep
%setup -q -c
# Go proxy zips contain the full module path as their archive prefix.
cp -a github.com/minio/console@%{module_version}/. .
rm -rf github.com
%autopatch -p1

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
