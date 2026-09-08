# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-vcr.v4
%define go_import_path  gopkg.in/dnaeon/go-vcr.v4

Name:           go-gopkg-dnaeon-go-vcr.v4
Version:        4.0.7
Release:        %autorelease
Summary:        HTTP interaction recorder and replayer for Go tests
License:        BSD-2-Clause
URL:            https://github.com/dnaeon/go-vcr
#!RemoteAsset:  sha256:0f9d5a1c4901375aa827b2ddc252ed9aa465a4d7e94725b1946964ec9804061f
Source0:        https://github.com/dnaeon/go-vcr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects printf directives in recorder tests.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(go.yaml.in/yaml/v4)

Provides:       go(gopkg.in/dnaeon/go-vcr.v4) = %{version}

Requires:       go(go.yaml.in/yaml/v4)

%description
Go-vcr records HTTP interactions and replays them in later test runs, enabling
fast, deterministic, and accurate testing of Go HTTP clients.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
