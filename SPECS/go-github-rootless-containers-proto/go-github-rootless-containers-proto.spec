# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           proto
%define go_import_path  github.com/rootless-containers/proto
%global commit_id       f6ee952d53d958e4583633302a7b3c1ae60b1adc

Name:           go-github-rootless-containers-proto
Version:        0.1.3+git20261020.f6ee952
Release:        %autorelease
Summary:        Protocol buffer definitions for rootless containers
License:        Apache-2.0
URL:            https://github.com/rootless-containers/proto
#!RemoteAsset:  sha256:a41174a3dce256ca86c968796ebfec3e4bea98d6c8c5e5801a6f7b73bd32d714
Source0:        https://github.com/rootless-containers/proto/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n proto-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)

Provides:       go(github.com/rootless-containers/proto) = %{version}

Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)

%description
This package contains the protocol buffer schema and generated Go
bindings for the user.rootlesscontainers extended attribute.

%files
%doc README.md
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
