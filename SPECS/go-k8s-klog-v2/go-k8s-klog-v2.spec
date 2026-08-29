# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           klog
%define go_import_path  k8s.io/klog/v2
# Example packages need optional test-only dependencies such as go-logr/zapr,
# go.uber.org/goleak and golang.org/x/tools/go/analysis/analysistest. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/examples*
}

Name:           go-k8s-klog-v2
Version:        2.140.0
Release:        %autorelease
Summary:        Leveled logging library for Go
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

Requires:       go(github.com/go-logr/logr)

%description
klog provides leveled logging for Go.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
