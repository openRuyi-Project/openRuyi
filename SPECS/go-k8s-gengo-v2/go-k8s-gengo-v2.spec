# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gengo
%define go_import_path  k8s.io/gengo
%define commit_id 25e2208e0dc371a827289e7faced19a2dbcd480b

Name:           go-k8s-gengo-v2
Version:        0+git20260607.25e2208
Release:        %autorelease
Summary:        Code generation helpers for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes/gengo
#!RemoteAsset:  sha256:ce4db405fd6f723cb5f9c51d4621fa2b9e9a824bcfd92e83beeefaec62325e04
Source0:        https://github.com/kubernetes/gengo/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The repository contains both k8s.io/gengo and k8s.io/gengo/v2 modules plus
# v1 examples; keep %check scoped to the v2 library packages exported here.
# Generator/parser tests use local testdata imports resolved as absolute
# filesystem paths under OBS GOPATH mode and fail before exercising themselves. - HNO3Miracle
%define go_test_include %{shrink:
    k8s.io/gengo/v2
    k8s.io/gengo/v2/codetags
    k8s.io/gengo/v2/namer
    k8s.io/gengo/v2/types
}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go-k8s-klog-v2
BuildRequires:  go(k8s.io/klog/v2)

Provides:       go(k8s.io/gengo) = %{version}
Provides:       go(k8s.io/gengo/v2) = %{version}

Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/spf13/pflag)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)
Requires:       go(k8s.io/klog/v2)

%description
This package provides Kubernetes code generation helpers for Go.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
