# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml
%define go_import_path  sigs.k8s.io/yaml

Name:           go-k8s-sigs-yaml
Version:        1.6.0
Release:        %autorelease
Summary:        Go library for sigs.k8s.io/yaml
License:        MIT
URL:            https://github.com/kubernetes-sigs/yaml
#!RemoteAsset:  sha256:a6c9c723642ed54ef74dab20c4158b6cef0f3f2afca34c1b402c1e5852b1720b
Source0:        https://github.com/kubernetes-sigs/yaml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n yaml-1.6.0

BuildRequires:  go
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go-rpm-macros

Provides:       go(sigs.k8s.io/yaml) = %{version}
Provides:       go(sigs.k8s.io/yaml/goyaml.v2) = %{version}
Provides:       go(sigs.k8s.io/yaml/goyaml.v3) = %{version}
Provides:       go(sigs.k8s.io/yaml/kyaml) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(sigs.k8s.io/randfill)

%description
This package provides the Go library sigs.k8s.io/yaml.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
