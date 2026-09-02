# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           raft
%define go_import_path  go.etcd.io/raft/v3

Name:           go-go.etcd-raft-v3
Version:        3.7.0
Release:        %autorelease
Summary:        Raft consensus algorithm implementation in Go
License:        Apache-2.0
URL:            https://github.com/etcd-io/raft
#!RemoteAsset:  sha256:d34da002dc4dfce876be1a40f95701a89465c7f1eaa36b896cd688ad48dcdd57
Source0:        https://github.com/etcd-io/raft/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cockroachdb/datadriven)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)

Provides:       go(go.etcd.io/raft/v3) = %{version}

Requires:       go(github.com/cockroachdb/datadriven)
Requires:       go(github.com/stretchr/testify)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)

%description
This package provides a Go implementation of the Raft consensus algorithm.
It is used by etcd to maintain a replicated state machine.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
