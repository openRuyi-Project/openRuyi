# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           casbin
%define go_import_path  github.com/casbin/casbin/v2

Name:           go-github-casbin-casbin-v2
Version:        2.135.0
Release:        %autorelease
Summary:        Authorization library supporting access control models
License:        Apache-2.0
URL:            https://github.com/casbin/casbin
#!RemoteAsset:  sha256:4e38bfd4ec2bef1b1803b4835f8cd781f1f0cba9f191f0bf93ffc89532ab2271
Source0:        https://github.com/casbin/casbin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects a legacy non-constant fmt.Errorf call in model;
# continue running the complete test suite. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bmatcuk/doublestar/v4)
BuildRequires:  go(github.com/casbin/govaluate)
BuildRequires:  go(github.com/golang/mock)
BuildRequires:  go(github.com/google/uuid)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/bmatcuk/doublestar/v4)
Requires:       go(github.com/casbin/govaluate)
Requires:       go(github.com/golang/mock)
Requires:       go(github.com/google/uuid)

%description
Casbin is an authorization library supporting ACL, RBAC, ABAC, and other
access control models in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
