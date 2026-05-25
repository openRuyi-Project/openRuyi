# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structured-merge-diff
%define go_import_path  sigs.k8s.io/structured-merge-diff/v6

Name:           go-k8s-sigs-structured-merge-diff-v6
Version:        6.3.0
Release:        %autorelease
Summary:        Kubernetes structured merge diff library for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/structured-merge-diff
#!RemoteAsset:  sha256:c999f87b2e21a207421f7319a9e83dff7a9a7d54244562fd9b9a6de780d10374
Source0:        https://github.com/kubernetes-sigs/structured-merge-diff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(sigs.k8s.io/randfill)

Provides:       go(sigs.k8s.io/structured-merge-diff/v6) = %{version}

%description
This package provides Kubernetes structured merge diff support for Go.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
