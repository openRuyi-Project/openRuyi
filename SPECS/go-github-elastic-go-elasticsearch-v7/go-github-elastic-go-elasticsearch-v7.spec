# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-elasticsearch
%define go_import_path  github.com/elastic/go-elasticsearch/v7

Name:           go-github-elastic-go-elasticsearch-v7
Version:        7.17.10
Release:        %autorelease
Summary:        Official Go client for Elasticsearch 7
License:        Apache-2.0
URL:            https://github.com/elastic/go-elasticsearch
#!RemoteAsset:  sha256:85f19702bd3ee29abfdeabb53875c761cfefa6b917ff1c519da2fe4c10752d0b
Source0:        https://github.com/elastic/go-elasticsearch/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Replace the removed x/crypto/ssh/terminal package with its maintained x/term
# successor in the repository's build tooling.
Patch2000:      2000-internal-build-use-x-term-for-terminal-detection.patch
# Accept expiry of the static certificate while retaining fingerprint checks.
Patch2001:      2001-test-accept-expiration-of-embedded-fingerprint-certi.patch
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/chroma)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(%{go_import_path}) = %{version}

%description
Go-elasticsearch is the official Go client for Elasticsearch. This package
provides the version 7 API.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
