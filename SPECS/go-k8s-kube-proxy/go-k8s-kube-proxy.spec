# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kube-proxy
%define go_import_path  k8s.io/kube-proxy

Name:           go-k8s-kube-proxy
Version:        0.19.3
Release:        %autorelease
Summary:        Kubernetes kube-proxy configuration API
License:        Apache-2.0
URL:            https://github.com/kubernetes/kube-proxy
#!RemoteAsset:  sha256:7d1aa1f1e5ab102ea19cc3480db0868a0676c8646ff5cbd95e9892107367963e
Source0:        https://github.com/kubernetes/kube-proxy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/component-base)

Provides:       go(k8s.io/kube-proxy) = %{version}

Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/component-base)

%description
This library provides the versioned configuration API and generated
deep-copy helpers for Kubernetes kube-proxy.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
