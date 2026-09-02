# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           molecule
%define go_import_path  github.com/richardartoul/molecule
%define commit          7ca0df43c0b3d9499ca618fb026b5d65179b6c11

Name:           go-github-richardartoul-molecule
Version:        1.0.0+git20260817.7ca0df4
Release:        %autorelease
Summary:        Zero-allocation protobuf parsing library for Go
License:        MIT
URL:            https://github.com/richardartoul/molecule
#!RemoteAsset:  sha256:e61edeb5bd0518eb5c620e91ec4828ba7b3a92ecc0fd33d86fea96675d851149
Source0:        https://github.com/richardartoul/molecule/archive/%{commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gotest.tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
Molecule provides a streaming, zero-allocation interface for selectively
parsing protobuf messages in performance-sensitive Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
