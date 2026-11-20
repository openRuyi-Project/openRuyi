# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           controller-runtime
%define go_import_path  sigs.k8s.io/controller-runtime

Name:           go-k8s-sigs-controller-runtime
Version:        0.24.1
Release:        %autorelease
Summary:        Libraries for building Kubernetes controllers
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/controller-runtime
#!RemoteAsset:  sha256:48cbc1c71f28c2a2cf533622c7b887724d2dc43930379d8667132bc21356c0a7
Source0:        https://github.com/kubernetes-sigs/controller-runtime/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/evanphx/json-patch/v5)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/zapr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gomodules.xyz/jsonpatch/v2)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apiextensions-apiserver)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/apiserver)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/evanphx/json-patch/v5)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/zapr)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/onsi/gomega)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(gomodules.xyz/jsonpatch/v2)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apiextensions-apiserver)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/apiserver)
Requires:       go(k8s.io/client-go)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)

%description
Controller Runtime provides libraries for building Kubernetes-style
controllers that work with built-in resources and custom resources.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
