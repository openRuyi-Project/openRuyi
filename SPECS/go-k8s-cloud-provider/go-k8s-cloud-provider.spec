# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cloud-provider
%define go_import_path  k8s.io/cloud-provider

Name:           go-k8s-cloud-provider
Version:        0.19.3
Release:        %autorelease
Summary:        Supplies interfaces and implementations for cloud service providers
License:        Apache-2.0
URL:            https://github.com/kubernetes/cloud-provider
#!RemoteAsset:  sha256:a1533ee9df65a1566232f0767ae22c93073266b9b380f77e0fe408052dd9cb20
Source0:        https://github.com/kubernetes/cloud-provider/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream replacements for APIs removed from current Kubernetes libraries.
# https://github.com/kubernetes/cloud-provider/commit/4b7a2d804e79314fd866210268a9bf7e2d35aa07
Patch1000:      1000-Replace-removed-NodeResources-type.patch
# https://github.com/kubernetes/cloud-provider/commit/3fefb5ab90595e1c6ea16334431cb684d199cc86
Patch1001:      1001-Remove-unused-rate-limiter-metrics.patch
# https://github.com/kubernetes/cloud-provider/commit/f993acddbd816ff241d1e3af1a5e9f06e75b7955
Patch1002:      1002-Update-fake-client-test-expectations.patch

# Legacy logging calls use non-constant formats rejected by current vet.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/component-base)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/utils)

Provides:       go(k8s.io/cloud-provider) = %{version}

Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)
Requires:       go(k8s.io/component-base)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/utils)

%description
This library defines the Kubernetes cloud provider interfaces and
initializes cloud provider implementations for controllers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
