# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           raft
%define go_import_path  go.etcd.io/raft

Name:           go-github-etcd-io-raft
Version:        3.6.0
Release:        %autorelease
Summary:        Raft library for maintaining a replicated state machine
License:        Apache-2.0
URL:            https://github.com/etcd-io/raft
#!RemoteAsset
Source0:        https://github.com/etcd-io/raft/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cockroachdb/datadriven)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(go.etcd.io/raft) = %{version}

Requires:       go(github.com/cockroachdb/datadriven)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/stretchr/testify)

%description
Raft is a protocol with which a cluster of nodes can maintain a
replicated state machine. The state machine is kept in sync through the
use of a replicated log. For more details on Raft, see "In Search of an
Understandable Consensus Algorithm" ((https://raft.github.io/raft.pdf))
by Diego Ongaro and John Ousterhout.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
