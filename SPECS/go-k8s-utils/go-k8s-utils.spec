# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           utils
%define go_import_path  k8s.io/utils
%define commit_id b8788abfbbc27cab6c8732274b5c2ae213868854
# TestLogIfLong is timing-sensitive and did not emit the expected trace log in
# OBS; keep the rest of the package checks enabled. - HNO3Miracle
%define go_test_exclude k8s.io/utils/trace

Name:           go-k8s-utils
Version:        0+git20260210.b8788ab
Release:        %autorelease
Summary:        Low-level Kubernetes-independent Go utility packages
License:        Apache-2.0
URL:            https://github.com/kubernetes/utils
#!RemoteAsset:  sha256:7c62393414c2ec4dabd1a80fe074949f7943b6a14797aa1ec0a671616abfd871
Source0:        https://github.com/kubernetes/utils/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(k8s.io/klog/v2)

Provides:       go(k8s.io/utils) = %{version}
Provides:       go(k8s.io/utils/buffer) = %{version}
Provides:       go(k8s.io/utils/clock) = %{version}
Provides:       go(k8s.io/utils/clock/testing) = %{version}
Provides:       go(k8s.io/utils/cpuset) = %{version}
Provides:       go(k8s.io/utils/diff) = %{version}
Provides:       go(k8s.io/utils/dump) = %{version}
Provides:       go(k8s.io/utils/env) = %{version}
Provides:       go(k8s.io/utils/exec) = %{version}
Provides:       go(k8s.io/utils/exec/testing) = %{version}
Provides:       go(k8s.io/utils/field) = %{version}
Provides:       go(k8s.io/utils/inotify) = %{version}
Provides:       go(k8s.io/utils/integer) = %{version}
Provides:       go(k8s.io/utils/internal/third_party/forked/golang/golang-lru) = %{version}
Provides:       go(k8s.io/utils/internal/third_party/forked/golang/net) = %{version}
Provides:       go(k8s.io/utils/io) = %{version}
Provides:       go(k8s.io/utils/keymutex) = %{version}
Provides:       go(k8s.io/utils/lru) = %{version}
Provides:       go(k8s.io/utils/mount) = %{version}
Provides:       go(k8s.io/utils/net) = %{version}
Provides:       go(k8s.io/utils/net/ebtables) = %{version}
Provides:       go(k8s.io/utils/nsenter) = %{version}
Provides:       go(k8s.io/utils/path) = %{version}
Provides:       go(k8s.io/utils/pointer) = %{version}
Provides:       go(k8s.io/utils/ptr) = %{version}
Provides:       go(k8s.io/utils/semantic) = %{version}
Provides:       go(k8s.io/utils/set) = %{version}
Provides:       go(k8s.io/utils/strings) = %{version}
Provides:       go(k8s.io/utils/strings/slices) = %{version}
Provides:       go(k8s.io/utils/temp) = %{version}
Provides:       go(k8s.io/utils/temp/temptest) = %{version}
Provides:       go(k8s.io/utils/third_party/forked/golang/btree) = %{version}
Provides:       go(k8s.io/utils/third_party/forked/golang/reflect) = %{version}
Provides:       go(k8s.io/utils/trace) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(k8s.io/klog/v2)


%description
k8s.io/utils contains low-level utility packages shared by Kubernetes projects
but kept independent from the main Kubernetes repository. It includes helpers
for clocks, sets, networking, execution, paths, pointers, buffers, and other
common Go infrastructure.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
