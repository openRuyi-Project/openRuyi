# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           randfill
%define go_import_path  sigs.k8s.io/randfill
# The root package only fails because Go 1.25 checks Example* names more
# strictly: ExampleSimple, ExampleSingle, etc. refer to non-existing symbols.
%define go_test_exclude sigs.k8s.io/randfill

Name:           go-k8s-sigs-randfill
Version:        1.0.0
Release:        %autorelease
Summary:        Go library for sigs.k8s.io/randfill
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/randfill
#!RemoteAsset:  sha256:681784c569991b6291697e68f91f9fba847a728c12c4aef82468b47b9678a6bc
Source0:        https://github.com/kubernetes-sigs/randfill/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n randfill-1.0.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(sigs.k8s.io/randfill) = %{version}
Provides:       go(sigs.k8s.io/randfill/bytesource) = %{version}

%description
This package provides the Go library sigs.k8s.io/randfill.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
