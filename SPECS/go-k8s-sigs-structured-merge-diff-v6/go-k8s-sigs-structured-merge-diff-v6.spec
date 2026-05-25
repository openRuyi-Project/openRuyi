# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structured-merge-diff
%define go_import_path  sigs.k8s.io/structured-merge-diff/v6
%define commit_id 2ad5e4f059c73f49f9c851b392ca3d4335c1c67e

Name:           go-k8s-sigs-structured-merge-diff-v6
Version:        0+git20260520.2ad5e4f
Release:        %autorelease
Summary:        Go library for sigs.k8s.io/structured-merge-diff/v6
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/structured-merge-diff
#!RemoteAsset:  sha256:f99cbfc7569d91fffc89acf087de28e091e948ae81f6b1b824d63383fa78442b
Source0:        https://github.com/kubernetes-sigs/structured-merge-diff/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go-rpm-macros

Provides:       go(sigs.k8s.io/structured-merge-diff/v6) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/fieldpath) = %{version}
Provides:       go(sigs.k8s.io/structured-merge-diff/v6/typed) = %{version}

%description
This package provides the Go library sigs.k8s.io/structured-merge-diff/v6.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
