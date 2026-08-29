# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-msgpack
%define go_import_path  github.com/hashicorp/go-msgpack
# The old codec test suite parses its own flags and rejects the standard
# go test flags (e.g. -test.testlogfile); run the tests but tolerate failure.
%define go_test_ignore_failure 1

Name:           go-github-hashicorp-go-msgpack
Version:        0.5.5
Release:        %autorelease
Summary:        Open-Source Go Code. msgpack.org[Go]
License:        MIT
URL:            https://github.com/hashicorp/go-msgpack
#!RemoteAsset:  sha256:a6a95afd348ce6f0be9183266d9479d8b8738097ff82b16345a78c7e26a37e13
Source0:        https://github.com/hashicorp/go-msgpack/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream test helper uses a non-constant format string that the current
# go vet rejects; disable vet (tests still run).
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-msgpack) = %{version}

%description
go-msgpack (codec) is a high-performance msgpack/json codec library for Go.
This package provides the v0.5.x release at the root import path
github.com/hashicorp/go-msgpack, used by hashicorp/memberlist, serf and
consul.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
