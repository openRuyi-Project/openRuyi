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
Summary:        YAML marshaling and unmarshaling support for Go
License:        (Apache-2.0 OR BSD-3-Clause OR MIT)
URL:            https://github.com/kubernetes-sigs/yaml
#!RemoteAsset:  sha256:a6c9c723642ed54ef74dab20c4158b6cef0f3f2afca34c1b402c1e5852b1720b
Source0:        https://github.com/kubernetes-sigs/yaml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(sigs.k8s.io/randfill)

Provides:       go(sigs.k8s.io/yaml) = %{version}
Provides:       go(sigs.k8s.io/yaml/goyaml.v2) = %{version}
Provides:       go(sigs.k8s.io/yaml/goyaml.v3) = %{version}
Provides:       go(sigs.k8s.io/yaml/kyaml) = %{version}
Provides:       go(sigs.k8s.io/yaml/yamlfmt) = %{version}

Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)


%description
sigs.k8s.io/yaml provides YAML marshaling and unmarshaling helpers for Go. It
wraps YAML handling in a way that fits Kubernetes JSON-compatible object
processing and is used across Kubernetes libraries.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
