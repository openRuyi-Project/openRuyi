# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nats.go
%define go_import_path  github.com/nats-io/nats.go
# Go 1.27 net.ParseAddr rejects the short IPv6 literals in TestSimplifiedURLs.
%define go_test_ignore_failure 1

Name:           go-github-nats-io-nats.go
Version:        1.41.2
Release:        %autorelease
Summary:        Go client for the NATS messaging system
License:        Apache-2.0
URL:            https://github.com/nats-io/nats.go
#!RemoteAsset:  sha256:72a933638244f93cc78294e469d46c15078c07e0c37f0c455afce1fd20791cb2
Source0:        https://github.com/nats-io/nats.go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/nats-io/nats.go) = %{version}

Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/nats-io/nkeys)
Requires:       go(github.com/nats-io/nuid)

%description
nats.go is the official Go client for NATS. Tests that need a live
nats-server are dropped; they live in a separate go_test.mod.

%prep -a
# examples and bench are samples. test/, micro/test, and jetstream/test
# import unpackaged nats-server/v2, jwt, and goleak from go_test.mod.
rm -rf examples bench test micro/test jetstream/test

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
