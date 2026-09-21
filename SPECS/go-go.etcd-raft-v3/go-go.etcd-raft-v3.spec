# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           raft
%define go_import_path  go.etcd.io/raft/v3

Name:           go-go.etcd-raft-v3
Version:        3.6.0
Release:        %autorelease
Summary:        Raft consensus algorithm implementation in Go
License:        Apache-2.0
URL:            https://github.com/etcd-io/raft
#!RemoteAsset:  sha256:b3f294a642494641a58a94c63db4fe5b080d7fb0ccdf97894d6d3fe735703179
Source0:        https://github.com/etcd-io/raft/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cockroachdb/datadriven)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(go.etcd.io/raft/v3) = %{version}

Requires:       go(github.com/cockroachdb/datadriven)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/stretchr/testify)

%description
This package provides a Go implementation of the Raft consensus algorithm.
It is used by etcd to maintain a replicated state machine.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
