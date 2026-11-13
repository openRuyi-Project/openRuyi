# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           godoc-lint
%define go_import_path  github.com/godoc-lint/godoc-lint

Name:           go-github-godoc-lint-godoc-lint
Version:        0.11.4
Release:        %autorelease
Summary:        Go documentation comment analyzer
License:        MIT
URL:            https://github.com/godoc-lint/godoc-lint
#!RemoteAsset:  sha256:5a9b5bef11e7faed1d191a76c1a9162c94164db54a98e4662495f54f19fbd9ee
Source0:        https://github.com/godoc-lint/godoc-lint/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(gopkg.in/yaml.v3)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/godoc-lint/godoc-lint) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/cmd/godoclint) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/analysis) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/deprecated) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/max_len) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/no_unused_link) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/pkg_doc) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/require_doc) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/shared) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/start_with_name) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/stdlib_doclink) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/stdlib_doclink/internal) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/check/stdlib_doclink/internal/gen) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/compose) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/config) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/inspect) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/model) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/util) = %{version}
Provides:       go(github.com/godoc-lint/godoc-lint/pkg/version) = %{version}

Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)

%description
Go documentation comment analyzer. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
