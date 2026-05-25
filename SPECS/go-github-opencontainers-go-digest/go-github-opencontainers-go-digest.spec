# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-digest
%define go_import_path  github.com/opencontainers/go-digest

Name:           go-github-opencontainers-go-digest
Version:        1.0.0~rc1
Release:        %autorelease
Summary:        Common digest package used across the container ecosystem
License:        Apache-2.0 AND CC-BY-SA-4.0
URL:            https://github.com/opencontainers/go-digest
#!RemoteAsset:  sha256:3f511b32c46f60482644f0ad6a345f52e672c82164bfb08274f15f7c14cd3076
Source0:        https://github.com/opencontainers/go-digest/archive/refs/tags/v1.0.0-rc1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-digest-1.0.0-rc1

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/opencontainers/go-digest) = %{version}


%description
go-digest

[Image: License] (https://img.shields.io/badge/License-Apache_2.0-
blue.svg) (https://opensource.org/licenses/Apache-2.0) [Image: Go
Reference] (https://pkg.go.dev/badge/opencontainers/go-digest)
(https://pkg.go.dev/github.com/opencontainers/go-digest) [Image: Go
Report Card]
(https://goreportcard.com/badge/github.com/opencontainers/go-digest)
(https://goreportcard.com/report/github.com/opencontainers/go-digest)
[Image: CI] (https://github.com/opencontainers/go-
digest/actions/workflows/test.yml/badge.svg)

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE.code
%license LICENSE.docs
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
