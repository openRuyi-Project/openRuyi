# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nats-server
%define go_import_path  github.com/nats-io/nats-server/v2
# The logger package requires a running syslog service; the server and AVL
# suites contain environment-sensitive cluster and performance tests.
%define go_test_exclude %{go_import_path}/logger %{go_import_path}/server %{go_import_path}/server/avl

Name:           go-github-nats-io-nats-server-v2
Version:        2.14.5
Release:        %autorelease
Summary:        NATS messaging server libraries for Go
License:        Apache-2.0
URL:            https://github.com/nats-io/nats-server
#!RemoteAsset:  sha256:e52606786923a346de676ae238889a79f55df61680f492ee5e2b1353b58418b5
Source0:        https://github.com/nats-io/nats-server/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects incorrect format verbs in two upstream tests.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/antithesishq/antithesis-sdk-go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/minio/highwayhash)
BuildRequires:  go(github.com/nats-io/jwt/v2)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/time)
# For tests
BuildRequires:  procps-ng

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/antithesishq/antithesis-sdk-go)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/minio/highwayhash)
Requires:       go(github.com/nats-io/jwt/v2)
Requires:       go(github.com/nats-io/nkeys)
Requires:       go(github.com/nats-io/nuid)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/time)

%description
This package provides the Go libraries from the NATS messaging server root
module.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
