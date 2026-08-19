# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protobuf-go-lite
%define go_import_path  github.com/aperturerobotics/protobuf-go-lite
# Generator integration tests invoke protoc and Go module commands, which are
# incompatible with the GOPATH mode required by the golangmodules build system.
# A cmd tool, -- Jvle
%define go_test_exclude  github.com/aperturerobotics/protobuf-go-lite/cmd/protoc-gen-go-lite

Name:           go-github-aperturerobotics-protobuf-go-lite
Version:        0.17.0
Release:        %autorelease
Summary:        Reflection-free Protobuf for Go.
License:        BSD-3-Clause
URL:            https://github.com/aperturerobotics/protobuf-go-lite
#!RemoteAsset:  sha256:315ef1596a07171b3a111048b8caebeb8a3d59fd4043d3836ab9370e8852fb8f
Source0:        https://github.com/aperturerobotics/protobuf-go-lite/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aperturerobotics/json-iterator-lite)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/aperturerobotics/protobuf-go-lite) = %{version}

Requires:       go(github.com/aperturerobotics/json-iterator-lite)
Requires:       go(google.golang.org/protobuf)

%description
protobuf-go-lite is a stripped-down version of the protobuf-go code
generator modified to work without reflection and merged with vtprotobuf
to provide modular features with static code generation for
marshal/unmarshal, size, clone, equal, text, and JSON. JSON support is
derived from a fork of protoc-gen-go-json.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
