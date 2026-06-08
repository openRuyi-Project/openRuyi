# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           klog
%define go_import_path  k8s.io/klog/v2
# The examples tree is documentation / benchmark code; OBS logs show it requires
# unpackaged optional example dependencies such as github.com/go-logr/zapr,
# go.uber.org/goleak, golang.org/x/tools/go/analysis/analysistest, and klog v1
# example helpers. - HNO3Miracle
%define go_test_exclude_glob k8s.io/klog/v2/examples*

Name:           go-k8s-klog-v2
Version:        2.140.0
Release:        %autorelease
Summary:        Kubernetes klog logging library for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes/klog
#!RemoteAsset:  sha256:2eb31b5b0f440396e4fdd69aea22e389583f084fa6afa4b02e992d551c04bba5
Source0:        https://github.com/kubernetes/klog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)

Provides:       go(k8s.io/klog/v2) = %{version}
Provides:       go(k8s.io/klog/v2/integration_tests/internal) = %{version}
Provides:       go(k8s.io/klog/v2/internal/buffer) = %{version}
Provides:       go(k8s.io/klog/v2/internal/clock) = %{version}
Provides:       go(k8s.io/klog/v2/internal/clock/testing) = %{version}
Provides:       go(k8s.io/klog/v2/internal/dbg) = %{version}
Provides:       go(k8s.io/klog/v2/internal/serialize) = %{version}
Provides:       go(k8s.io/klog/v2/internal/severity) = %{version}
Provides:       go(k8s.io/klog/v2/internal/sloghandler) = %{version}
Provides:       go(k8s.io/klog/v2/internal/test) = %{version}
Provides:       go(k8s.io/klog/v2/internal/test/require) = %{version}
Provides:       go(k8s.io/klog/v2/internal/verbosity) = %{version}
Provides:       go(k8s.io/klog/v2/klogr) = %{version}
Provides:       go(k8s.io/klog/v2/ktesting) = %{version}
Provides:       go(k8s.io/klog/v2/ktesting/init) = %{version}
Provides:       go(k8s.io/klog/v2/test) = %{version}
Provides:       go(k8s.io/klog/v2/textlogger) = %{version}

Requires:       go(github.com/go-logr/logr)


%description
klog v2 is the current Kubernetes logging library for Go. It provides the
logging API, logr integration, testing helpers, and text logger support used by
newer Kubernetes modules.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
