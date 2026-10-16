# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structured-merge-diff
%define go_import_path  sigs.k8s.io/structured-merge-diff/v4

Name:           go-k8s-sigs-structured-merge-diff-v4
Version:        4.0.1
Release:        %autorelease
Summary:        Kubernetes structured merge and diff library for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/structured-merge-diff
#!RemoteAsset:  sha256:97fe500d1378fe8cf233f590f10dda77020d34aa789595c13947aa4dbe9fee99
Source0:        https://github.com/kubernetes-sigs/structured-merge-diff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects non-constant format strings in this release.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(sigs.k8s.io/structured-merge-diff/v4) = %{version}

Requires:       go(github.com/json-iterator/go)
Requires:       go(gopkg.in/yaml.v2)

%description
This library implements structured merge and diff operations for
Kubernetes, including schemas, field ownership and conflict detection.

%prep -a
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
