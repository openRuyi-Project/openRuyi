# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cluster-bootstrap
%define go_import_path  k8s.io/cluster-bootstrap

Name:           go-k8s-cluster-bootstrap
Version:        0.19.3
Release:        %autorelease
Summary:        Kubernetes cluster bootstrap token helpers
License:        Apache-2.0
URL:            https://github.com/kubernetes/cluster-bootstrap
#!RemoteAsset:  sha256:863778ec703a33cc7c019b0505d49f41a30b6def62316f4422a705593932c379
Source0:        https://github.com/kubernetes/cluster-bootstrap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/square/go-jose.v2)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/klog/v2)

Provides:       go(k8s.io/cluster-bootstrap) = %{version}

Requires:       go(gopkg.in/square/go-jose.v2)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/klog/v2)

%description
This library provides bootstrap token constants, validation, signing
and secret helpers used by Kubernetes cluster bootstrap components.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
