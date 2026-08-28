# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nats.go
%define go_import_path  github.com/nats-io/nats.go
# The test subpackages use the external NATS Testing Framework service via
# orbit.go/ntf-client. That client depends on nats.go itself, so the service
# tests would create a build cycle and are not runnable in OBS.
%define go_test_exclude_glob %{go_import_path}/test* %{go_import_path}/jetstream/test* %{go_import_path}/micro/test*

Name:           go-github-nats-io-nats.go
Version:        1.53.1
Release:        %autorelease
Summary:        Go client for the NATS messaging system
License:        Apache-2.0
URL:            https://github.com/nats-io/nats.go
#!RemoteAsset:  sha256:633e9fd0791b6e9732b9754b83542fbdc5059da6588b1145d1a2c69904b8e188
Source0:        https://github.com/nats-io/nats.go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/nats-io/jwt/v2)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(google.golang.org/protobuf/proto)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/nats-io/nkeys)
Requires:       go(github.com/nats-io/nuid)
Requires:       go(google.golang.org/protobuf/proto)

%description
NATS.go is the official Go client for the NATS messaging system.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
