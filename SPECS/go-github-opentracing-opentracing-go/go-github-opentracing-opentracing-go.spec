# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentracing-go
%define go_import_path  github.com/opentracing/opentracing-go

Name:           go-github-opentracing-opentracing-go
Version:        1.2.0
Release:        %autorelease
Summary:        OpenTracing API for Go
License:        Apache-2.0
URL:            https://github.com/opentracing/opentracing-go
#!RemoteAsset:  sha256:cb32b383422a9aae11d260657d52a3789bd799802881b9ced3ee82c370be6f76
Source0:        https://github.com/opentracing/opentracing-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/opentracing/opentracing-go) = %{version}

%description
A Go API for OpenTracing instrumentation. It defines interfaces and helpers for
creating, propagating, and recording distributed tracing spans.

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
