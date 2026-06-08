# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           randfill
%define go_import_path  sigs.k8s.io/randfill
# Go 1.25 checks Example* names more strictly, and the root package examples
# refer to non-existing symbols such as ExampleSimple and ExampleSingle. - HNO3Miracle
%define go_test_exclude sigs.k8s.io/randfill

Name:           go-k8s-sigs-randfill
Version:        1.0.0
Release:        %autorelease
Summary:        Random Go object population library
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/randfill
#!RemoteAsset:  sha256:681784c569991b6291697e68f91f9fba847a728c12c4aef82468b47b9678a6bc
Source0:        https://github.com/kubernetes-sigs/randfill/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(sigs.k8s.io/randfill) = %{version}
Provides:       go(sigs.k8s.io/randfill/bytesource) = %{version}


%description
randfill is a helper library for populating Go objects with random values in
tests. Kubernetes structured merge and API machinery tests use it to exercise
serialization and merge behavior across generated object graphs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
