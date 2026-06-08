# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           klog
%define go_import_path  k8s.io/klog
# klogr packages in klog v1.0.0 target the old logr API; OBS has logr 1.4.3 and fails with
# undefined logr.InfoLogger / incompatible logr.Logger types. TestRollover in
# the root package is unstable in OBS because the log file name and size do not
# reset after rotation. - HNO3Miracle
%define go_test_exclude %{shrink:
    %{go_import_path}
    k8s.io/klog/examples/klogr
    k8s.io/klog/klogr
}

Name:           go-k8s-klog
Version:        1.0.0
Release:        %autorelease
Summary:        Implements logging analogous to the Google-internal C++ INFO/ERROR/V setup
License:        Apache-2.0
URL:            https://github.com/kubernetes/klog
#!RemoteAsset:  sha256:eb84fc7a8051175f2da4a428360ce70703c8ccdd0e987fddc2f9d5c8fd97cd00
Source0:        https://github.com/kubernetes/klog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
# Go 1.25 vet rejects integration_tests/internal/main.go with non-constant
# fmt.Fprintf format strings; keep tests enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/golang/glog)

Provides:       go(k8s.io/klog) = %{version}
Provides:       go(k8s.io/klog/examples/coexist_glog) = %{version}
Provides:       go(k8s.io/klog/examples/klogr) = %{version}
Provides:       go(k8s.io/klog/examples/log_file) = %{version}
Provides:       go(k8s.io/klog/examples/set_output) = %{version}
Provides:       go(k8s.io/klog/integration_tests/internal) = %{version}
Provides:       go(k8s.io/klog/klogr) = %{version}

Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/golang/glog)

%description
klog is the original Kubernetes logging library for Go. It implements
INFO/ERROR/V-style logging and compatibility helpers needed by older
Kubernetes-related Go modules.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
