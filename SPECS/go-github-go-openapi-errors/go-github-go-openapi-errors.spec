# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errors
%define go_import_path  github.com/go-openapi/errors

Name:           go-github-go-openapi-errors
Version:        0.22.7
Release:        %autorelease
Summary:        Common error definitions used across the go-openapi projects
License:        Apache-2.0
URL:            https://github.com/go-openapi/errors
#!RemoteAsset:  sha256:e8efab860f5627ac492e7d69f0e354ce0388fa85c35a726d129c321c177e968a
Source0:        https://github.com/go-openapi/errors/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# No runtime dependencies; the tests use go-openapi/testify/v2.
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/testify/v2)

Provides:       go(github.com/go-openapi/errors) = %{version}

%description
This package provides the common error types and helpers shared across
the go-openapi and go-swagger projects (typed API errors, composite
errors, and HTTP status helpers). It is a runtime dependency of
go-openapi/strfmt, which Prometheus uses.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
