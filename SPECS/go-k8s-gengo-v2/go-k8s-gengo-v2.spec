# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gengo
%define go_import_path  k8s.io/gengo
%define commit_id       85fd79dbfd9fc7a328697266cbb852e1857ec2a0
# The repository contains both k8s.io/gengo and k8s.io/gengo/v2 modules.
# Keep %check scoped to v2 packages that do not hit the current x/tools
# tokeninternal build breakage or local testdata path handling. - HNO3Miracle
%define go_test_include %{shrink:
    k8s.io/gengo/v2/codetags
    k8s.io/gengo/v2/namer
    k8s.io/gengo/v2/types
}

Name:           go-k8s-gengo-v2
Version:        0+git20250604.85fd79d
Release:        %autorelease
Summary:        Kubernetes code generation helpers for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes/gengo
#!RemoteAsset:  sha256:82a58d47726f05bf00a1e33a69130dfae32266c2f0004a869cf3ecba4abea5e1
Source0:        https://github.com/kubernetes/gengo/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# GitHub commit archives unpack to gengo-%{commit_id}; keep the explicit
# source directory instead of relying on a tag-style default. - HNO3Miracle
BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(k8s.io/klog/v2)

Provides:       go(k8s.io/gengo/v2) = %{version}
Provides:       go(k8s.io/gengo/v2/codetags) = %{version}
Provides:       go(k8s.io/gengo/v2/examples/kilroy) = %{version}
Provides:       go(k8s.io/gengo/v2/examples/pointuh) = %{version}
Provides:       go(k8s.io/gengo/v2/examples/tracer) = %{version}
Provides:       go(k8s.io/gengo/v2/generator) = %{version}
Provides:       go(k8s.io/gengo/v2/namer) = %{version}
Provides:       go(k8s.io/gengo/v2/parser) = %{version}
Provides:       go(k8s.io/gengo/v2/parser/tags) = %{version}
Provides:       go(k8s.io/gengo/v2/types) = %{version}

Requires:       go(github.com/spf13/pflag)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/tools)
Requires:       go(k8s.io/klog/v2)

%description
gengo provides Kubernetes code generation helpers for Go source trees. It
includes parsers, namers, and generator support used by kube-openapi and other
Kubernetes tools that derive generated code from Go API types.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
