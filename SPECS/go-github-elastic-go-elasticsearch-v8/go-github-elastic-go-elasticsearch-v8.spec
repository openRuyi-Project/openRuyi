# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-elasticsearch
%define go_import_path  github.com/elastic/go-elasticsearch/v8

Name:           go-github-elastic-go-elasticsearch-v8
Version:        8.19.7
Release:        %autorelease
Summary:        Official Go client for Elasticsearch 8
License:        Apache-2.0
URL:            https://github.com/elastic/go-elasticsearch
#!RemoteAsset:  sha256:c619cb18fcb3f3dadcaed7f34b5dee21a6edd2c20f91dba561db330aca2bee6d
Source0:        https://github.com/elastic/go-elasticsearch/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Replace the removed x/crypto/ssh/terminal package with its maintained x/term
# successor in the repository's build tooling.
Patch2000:      2000-internal-build-use-x-term-for-terminal-detection.patch
# Fix snapshot fallback and preserve legacy UTC timestamp serialization.
Patch2001:      2001-internal-build-fix-snapshot-fallback-and-timestamp-f.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/chroma)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/elastic/elastic-transport-go/v8)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/elastic/elastic-transport-go/v8)
Requires:       go(go.opentelemetry.io/otel)

%description
Go-elasticsearch is the official Go client for Elasticsearch. This package
provides the version 8 API.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
