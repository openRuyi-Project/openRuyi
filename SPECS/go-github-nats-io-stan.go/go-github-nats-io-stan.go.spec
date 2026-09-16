# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stan.go
%define go_import_path  github.com/nats-io/stan.go

Name:           go-github-nats-io-stan.go
Version:        0.10.4
Release:        %autorelease
Summary:        Go client for NATS Streaming
License:        Apache-2.0
URL:            https://github.com/nats-io/stan.go
#!RemoteAsset:  sha256:cc432ec80ab7d933ac1fc47f02da29e3ae7eb240c83b1d7251931475e5c2212c
Source0:        https://github.com/nats-io/stan.go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nuid)

Provides:       go(github.com/nats-io/stan.go) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/nats-io/nats.go)
Requires:       go(github.com/nats-io/nuid)

%description
stan.go is the Go client for NATS Streaming. Tests that need a live
nats-server and nats-streaming-server live in a separate go_tests.mod.

%prep -a
# examples are samples. Root tests import unpackaged nats-server/v2 and
# nats-streaming-server from go_tests.mod.
rm -rf examples
rm -f stan_test.go benchmark_test.go

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
