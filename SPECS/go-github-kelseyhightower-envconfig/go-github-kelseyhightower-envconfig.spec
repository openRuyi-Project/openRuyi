# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           envconfig
%define go_import_path  github.com/kelseyhightower/envconfig

Name:           go-github-kelseyhightower-envconfig
Version:        1.4.0
Release:        %autorelease
Summary:        Decode environment variables into Go structs
License:        MIT
URL:            https://github.com/kelseyhightower/envconfig
#!RemoteAsset:  sha256:c4f58ccab8b01b4b990ed3d31c09c0b41209a3a2b79c89b263090b91b69896d7
Source0:        https://github.com/kelseyhightower/envconfig/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Newer vet rejects the quoted integer diagnostics in the 1.4.0 tests.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
envconfig populates Go structs from environment variables. It supports
struct tags, default and required values, embedded structs, collections,
and custom decoders.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
