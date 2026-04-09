# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protobuf
%define go_import_path  google.golang.org/protobuf

Name:           go-google-protobuf
Version:        1.36.11
Release:        %autorelease
Summary:        Go support for Google's protocol buffers
License:        BSD-3-Clause
URL:            https://github.com/protocolbuffers/protobuf-go
#!RemoteAsset
Source0:        https://github.com/protocolbuffers/protobuf-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(google.golang.org/protobuf) = %{version}

Requires:       pkgconfig(protobuf)

%description
This project hosts the Go implementation for protocol buffers
(https://protobuf.dev), which is a language-neutral, platform-neutral,
extensible mechanism for serializing structured data. The protocol
buffer language is a language for specifying the schema for structured
data. This schema is compiled into language specific bindings. This
project provides both a tool to generate Go code for the protocol buffer
language, and also the runtime implementation to handle serialization of
messages in Go. See the protocol buffer developer guide
(https://protobuf.dev/overview) for more information about protocol
buffers themselves.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
