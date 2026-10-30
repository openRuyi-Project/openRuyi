# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golines
%define go_import_path  github.com/golangci/golines

Name:           go-github-golangci-golines
Version:        0.16.0
Release:        %autorelease
Summary:        Go formatter for shortening long lines
License:        MIT
URL:            https://github.com/golangci/golines
#!RemoteAsset:  sha256:5745f0e490033ae8eb2f9d731cd7a6b5efe2a5b71a830a6cb9900f4140c4d322
Source0:        https://github.com/golangci/golines/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/kingpin/v2)
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/dave/dst)
BuildRequires:  go(github.com/dave/dst/decorator)
BuildRequires:  go(github.com/dave/dst/gendst/data)
BuildRequires:  go(github.com/dave/jennifer)
BuildRequires:  go(github.com/dave/jennifer/jen)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/ldez/structtags)
BuildRequires:  go(github.com/ldez/structtags/parser)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/rogpeppe/go-internal/diff)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(github.com/xhit/go-str2duration/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/semaphore)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/imports)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/golines) = %{version}
Provides:       go(github.com/golangci/golines/internal/diff) = %{version}
Provides:       go(github.com/golangci/golines/internal/formatter) = %{version}
Provides:       go(github.com/golangci/golines/shorten) = %{version}
Provides:       go(github.com/golangci/golines/shorten/internal) = %{version}
Provides:       go(github.com/golangci/golines/shorten/internal/annotation) = %{version}
Provides:       go(github.com/golangci/golines/shorten/internal/comments) = %{version}
Provides:       go(github.com/golangci/golines/shorten/internal/generate) = %{version}
Provides:       go(github.com/golangci/golines/shorten/internal/graph) = %{version}
Provides:       go(github.com/golangci/golines/shorten/internal/tags) = %{version}

Requires:       go(github.com/alecthomas/kingpin/v2)
Requires:       go(github.com/dave/dst)
Requires:       go(github.com/dave/dst/decorator)
Requires:       go(github.com/dave/dst/gendst/data)
Requires:       go(github.com/dave/jennifer/jen)
Requires:       go(github.com/ldez/structtags/parser)
Requires:       go(github.com/rogpeppe/go-internal/diff)
Requires:       go(golang.org/x/sync/semaphore)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/tools/imports)

%description
Go formatter for shortening long lines. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
