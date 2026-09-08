# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cel-go
%define go_import_path  github.com/google/cel-go
# These packages require stable timing, Bazel runfiles, or pre-Go 1.26 output.
%define go_test_exclude %{shrink:
    %{go_import_path}/cel
    %{go_import_path}/conformance/policy
    %{go_import_path}/ext
}

Name:           go-github-google-cel-go
Version:        0.31.0
Release:        %autorelease
Summary:        Common Expression Language implementation for Go
License:        Apache-2.0
URL:            https://github.com/google/cel-go
#!RemoteAsset:  sha256:034bf0d7e03fe1423510c209368f8b441d987b9b0ed494088fe93901b96ecf17
Source0:        https://github.com/google/cel-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cel.dev/expr/conformance)
BuildRequires:  go(github.com/antlr4-go/antlr/v4)
BuildRequires:  go(github.com/bazelbuild/rules_go/go/runfiles)
BuildRequires:  go(github.com/chzyer/readline)
BuildRequires:  go(github.com/golang/glog)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  tzdata

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(cel.dev/expr/conformance)
Requires:       go(github.com/antlr4-go/antlr/v4)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/protobuf)

%description
CEL-Go implements the Common Expression Language for safe, portable, and
non-Turing-complete expression evaluation in Go applications.

%prep -a
rm -rf vendor

%check -a
# Compile packages whose runtime tests are incompatible with the OBS worker.
go test -vet=off -run '^$' %{go_test_exclude}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
