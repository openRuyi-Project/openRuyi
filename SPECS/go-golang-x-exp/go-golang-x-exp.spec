# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           exp
%define go_import_path  golang.org/x/exp
# Upstream does not provide proper git tags, use commit ID instead - 251
%define commit_id 3dfff04db8fa6b6338ec60a0317f99db30637e41
# So tired, can't stand more flaky tests - 251
%define go_test_exclude_glob %{shrink:
    golang.org/x/exp/apidiff*
    golang.org/x/exp/constraints*
    golang.org/x/exp/cmd*
    golang.org/x/exp/errors*
    golang.org/x/exp/event*
    golang.org/x/exp/typeparams/example*
    golang.org/x/exp/jsonrpc2*
    golang.org/x/exp/shiny*
    golang.org/x/exp/slog/benchmarks/zap_benchmarks*
    golang.org/x/exp/slog/benchmarks/zerolog_benchmarks*
    golang.org/x/exp/sumdb*
}

Name:           go-golang-x-exp
Version:        0+git20260721.3dfff04
Release:        %autorelease
Summary:        Experimental and deprecated packages
License:        BSD-3-Clause
URL:            https://golang.org/x/exp
VCS:            git:https://github.com/golang/exp
#!RemoteAsset:  sha256:cf025453112f46fa81f147dbdf8a6685014d0924bf93fc2318762c1a96cbc2c8
Source0:        https://github.com/golang/exp/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport upstream commit c3855c9 for Go 1.27 API consistency tests.
Patch2000:      2000-typeparams-consider-string-methods-optional.patch

BuildOption(check):  -vet=off -short

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(golang.org/x/exp) = %{version}
Provides:       go(golang.org/x/exp/typeparams) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/tools)

%description
This package holds experimental and deprecated (in the old directory) packages.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
