# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structured-merge-diff
%define go_import_path  sigs.k8s.io/structured-merge-diff/v6

Name:           go-k8s-sigs-structured-merge-diff-v6
Version:        6.3.2
Release:        %autorelease
Summary:        Kubernetes structured merge and diff library for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/structured-merge-diff
#!RemoteAsset:  sha256:3f6d2457052bfda9f91bf352c9a10e3a18e65599ee490322b46235f8d79c8b2f
Source0:        https://github.com/kubernetes-sigs/structured-merge-diff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(sigs.k8s.io/randfill)

Provides:       go(sigs.k8s.io/structured-merge-diff/v6) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/fieldpath) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/internal/cli) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/internal/fixture) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/merge) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/schema) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/smd) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/typed) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/value) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/json-iterator/go)
Requires:       go(go.yaml.in/yaml/v2)


%description
structured-merge-diff implements typed value comparison, merging, and field
path tracking for Kubernetes-style objects. Kubernetes uses it for server-side
apply and managed fields processing.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
