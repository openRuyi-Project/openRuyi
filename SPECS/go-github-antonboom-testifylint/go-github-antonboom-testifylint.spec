# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testifylint
%define go_import_path  github.com/Antonboom/testifylint

Name:           go-github-antonboom-testifylint
Version:        1.6.4
Release:        %autorelease
Summary:        Go analyzer for Testify assertion usage
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            https://github.com/Antonboom/testifylint
#!RemoteAsset:  sha256:d673d97771baaa406831f692181963ec682497f77c2dcdab6fdec89d8b4389ca
Source0:        https://github.com/Antonboom/testifylint/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/ghetzel/testify)
BuildRequires:  go(github.com/ghetzel/testify/require)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/pmezard/go-difflib/difflib)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/http)
BuildRequires:  go(github.com/stretchr/testify/mock)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(github.com/stretchr/testify/suite)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)
BuildRequires:  go(golang.org/x/tools/go/types/typeutil)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/Antonboom/testifylint) = %{version}
Provides:       go(github.com/Antonboom/testifylint/analyzer) = %{version}
Provides:       go(github.com/Antonboom/testifylint/internal/analysisutil) = %{version}
Provides:       go(github.com/Antonboom/testifylint/internal/checkers) = %{version}
Provides:       go(github.com/Antonboom/testifylint/internal/checkers/printf) = %{version}
Provides:       go(github.com/Antonboom/testifylint/internal/config) = %{version}
Provides:       go(github.com/Antonboom/testifylint/internal/testgen) = %{version}
Provides:       go(github.com/Antonboom/testifylint/internal/testify) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)
Requires:       go(golang.org/x/tools/go/types/typeutil)

%description
Go analyzer for Testify assertion usage. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%license analyzer/testdata/src/vendor/github.com/davecgh/go-spew/LICENSE
%license analyzer/testdata/src/vendor/github.com/ghetzel/testify/LICENSE
%license analyzer/testdata/src/vendor/github.com/go-logr/logr/LICENSE
%license analyzer/testdata/src/vendor/github.com/go-task/slim-sprig/v3/LICENSE.txt
%license analyzer/testdata/src/vendor/github.com/google/pprof/LICENSE
%license analyzer/testdata/src/vendor/github.com/onsi/ginkgo/v2/LICENSE
%license analyzer/testdata/src/vendor/github.com/pmezard/go-difflib/LICENSE
%license analyzer/testdata/src/vendor/github.com/stretchr/objx/LICENSE
%license analyzer/testdata/src/vendor/github.com/stretchr/testify/LICENSE
%license analyzer/testdata/src/vendor/golang.org/x/sys/LICENSE
%license analyzer/testdata/src/vendor/golang.org/x/tools/LICENSE
%license analyzer/testdata/src/vendor/gopkg.in/yaml.v2/LICENSE
%license analyzer/testdata/src/vendor/gopkg.in/yaml.v2/LICENSE.libyaml
%license analyzer/testdata/src/vendor/gopkg.in/yaml.v2/NOTICE
%license analyzer/testdata/src/vendor/gopkg.in/yaml.v3/LICENSE
%license analyzer/testdata/src/vendor/gopkg.in/yaml.v3/NOTICE
%license internal/checkers/printf/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
