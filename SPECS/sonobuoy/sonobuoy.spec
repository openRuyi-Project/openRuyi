# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sonobuoy
%define go_import_path  github.com/vmware-tanzu/sonobuoy

Name:           sonobuoy
Version:        0.57.3
Release:        %autorelease
Summary:        Kubernetes cluster conformance and diagnostics tool
License:        Apache-2.0
URL:            https://github.com/vmware-tanzu/sonobuoy
#!RemoteAsset:  sha256:d581032898c17f1df6db90e85aae8dae6429e8cd2a1b54e1728ddeaa7d9a989c
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# RISC-V smoke-test manifest installed with the package.
Source1:        openruyi-riscv-sonobuoy-smoke.yaml
BuildSystem:    golang

# Adapt the upstream IPv4 aggregator address fix for v%{version}.
# https://github.com/vmware-tanzu/sonobuoy/commit/08e4ff4475e5e30c596dc6f8ff94708b3750f9d4
Patch0:         0001-config-format-advertise-ip-with-net.JoinHostPort.patch
# Backport upstream test-format fixes for the current Go printf analyzer.
# https://github.com/vmware-tanzu/sonobuoy/commit/08e4ff4475e5e30c596dc6f8ff94708b3750f9d4
Patch1000:      1000-tests-use-constant-formats-for-fixture-strings.patch

BuildRequires:  go >= 1.23
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/briandowns/spinner)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/rifflock/lfshook)
BuildRequires:  go(github.com/satori/go.uuid)
BuildRequires:  go(github.com/sethgrid/pester)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/api/apps/v1)
BuildRequires:  go(k8s.io/api/core/v1)
BuildRequires:  go(k8s.io/api/rbac/v1)
BuildRequires:  go(k8s.io/apimachinery/pkg)
BuildRequires:  go(k8s.io/apimachinery/pkg/version)
BuildRequires:  go(k8s.io/client-go/discovery)
BuildRequires:  go(k8s.io/client-go/dynamic)
BuildRequires:  go(k8s.io/client-go/kubernetes)
BuildRequires:  go(k8s.io/client-go/plugin)
BuildRequires:  go(k8s.io/client-go/rest)
BuildRequires:  go(k8s.io/client-go/restmapper)
BuildRequires:  go(k8s.io/client-go/testing)
BuildRequires:  go(k8s.io/client-go/tools)
BuildRequires:  go(k8s.io/client-go/util)
BuildRequires:  go(k8s.io/klog)
BuildRequires:  go(sigs.k8s.io/yaml)

Recommends:     kubernetes

%description
Sonobuoy is a diagnostic tool that makes it easier to understand the state of a
Kubernetes cluster by running plugins, collecting results, and producing a
portable result bundle.

%install -a
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/openruyi-riscv-sonobuoy-smoke.yaml

%check -a
%{buildroot}%{_bindir}/%{name} version
%{buildroot}%{_bindir}/%{name} gen plugin --help >/dev/null

%files
%doc README.md CONTRIBUTING.md SECURITY.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/openruyi-riscv-sonobuoy-smoke.yaml

%changelog
%autochangelog
