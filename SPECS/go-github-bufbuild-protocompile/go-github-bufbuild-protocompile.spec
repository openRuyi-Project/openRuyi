# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protocompile
%define go_import_path  github.com/bufbuild/protocompile
# internal/tools is only used by upstream generate/lint targets, and
# internal/benchmarks depends on the predecessor parser for comparisons.
# linker tests require upstream's generated ../.tmp/cache/protoc/27.0/bin/protoc
# from `make protoc`; the remaining packages still run their normal Go tests.
# - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    github.com/bufbuild/protocompile/internal/tools
    github.com/bufbuild/protocompile/internal/benchmarks
    github.com/bufbuild/protocompile/linker
    github.com/bufbuild/protocompile/parser
}

Name:           go-github-bufbuild-protocompile
Version:        0.14.1
Release:        %autorelease
Summary:        Protobuf parser and linker engine for Go
License:        Apache-2.0
URL:            https://github.com/bufbuild/protocompile
#!RemoteAsset:  sha256:321593b96692d8a821a205d75340c69cf187dfbd59ba146ed50957a3dfe214ef
Source0:        https://github.com/bufbuild/protocompile/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/bufbuild/protocompile) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/sync)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)

%description
protocompile provides a parser, linker, and compiler for Protocol Buffer
source files.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
