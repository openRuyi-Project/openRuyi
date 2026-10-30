# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           conc
%define go_import_path  github.com/sourcegraph/conc

Name:           go-github-sourcegraph-conc
Version:        0.3.0
Release:        %autorelease
Summary:        Structured concurrency helpers for Go
License:        MIT
URL:            https://github.com/sourcegraph/conc
#!RemoteAsset:  sha256:c20a36ef6e8cd4721b8824d3e0a590d78f56ce72ace53ec7fdd2f7a978e9240f
Source0:        https://github.com/sourcegraph/conc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/sourcegraph/conc) = %{version}
Provides:       go(github.com/sourcegraph/conc/iter) = %{version}
Provides:       go(github.com/sourcegraph/conc/panics) = %{version}
Provides:       go(github.com/sourcegraph/conc/pool) = %{version}
Provides:       go(github.com/sourcegraph/conc/stream) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.uber.org/atomic)
Requires:       go(go.uber.org/multierr)
Requires:       go(gopkg.in/check.v1)
Requires:       go(gopkg.in/yaml.v3)

%description
Conc provides scoped goroutines, worker pools, and concurrent iteration
helpers with panic propagation and explicit lifetime management.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
