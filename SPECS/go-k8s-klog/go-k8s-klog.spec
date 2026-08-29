# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           klog
%define go_import_path  k8s.io/klog
# klogr in klog 0.x targets the pre-v1 go-logr API and does not build with the
# packaged go-logr 1.4; keep the k8s.io/klog v1 module package scoped to klog. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/examples/klogr*
    %{go_import_path}/klogr*
}

Name:           go-k8s-klog
Version:        1.0.0
Release:        %autorelease
Summary:        Leveled execution logs for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes/klog
#!RemoteAsset:  sha256:eb84fc7a8051175f2da4a428360ce70703c8ccdd0e987fddc2f9d5c8fd97cd00
Source0:        https://github.com/kubernetes/klog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix Go vet non-constant format failures and timing-sensitive logging tests
# with the current packaged Go toolchain. - HNO3Miracle
Patch2000:      2000-fix-tests-for-current-toolchain.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/glog)

Provides:       go(k8s.io/klog) = %{version}

Requires:       go(github.com/golang/glog)

%description
klog is a permanent fork of github.com/golang/glog.

# klog v1 bundles klogr directories that target the incompatible k8s.io/klog/v2
# module path. Remove them from buildroot so automatic Go provides do not
# collide with the dedicated go-k8s-klog-v2 package. - HNO3Miracle
%install -a
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/examples/klogr \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/klogr

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
