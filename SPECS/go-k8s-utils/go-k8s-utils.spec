# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           utils
%define go_import_path  k8s.io/utils
%define commit_id ff6756f316d28f49a7aab7ba7dddb0e526a1e35b
# TestLogIfLong is timing-sensitive and did not emit the expected trace log in OBS. - HNO3Miracle
%define go_test_exclude k8s.io/utils/trace

Name:           go-k8s-utils
Version:        0+git20260607.ff6756f
Release:        %autorelease
Summary:        Utility packages for Kubernetes Go components
License:        Apache-2.0
URL:            https://github.com/kubernetes/utils
#!RemoteAsset:  sha256:0882bdac456bcf478979c8fec6ae802f29c531a4b317b2286f569f0c84887fa2
Source0:        https://github.com/kubernetes/utils/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go-k8s-klog-v2
BuildRequires:  go(k8s.io/klog/v2)

Provides:       go(k8s.io/utils) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/go-logr/logr)
Requires:       go(k8s.io/klog/v2)

%description
This package provides utility packages shared by Kubernetes Go components.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
