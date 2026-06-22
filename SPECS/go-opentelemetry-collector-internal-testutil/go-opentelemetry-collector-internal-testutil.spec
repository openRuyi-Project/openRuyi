# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testutil
%define go_import_path  go.opentelemetry.io/collector/internal/testutil
# Keep %check scoped to this module so GOPATH-mode tests do not scan sibling
# modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-opentelemetry-collector-internal-testutil
Version:        0.152.0
Release:        %autorelease
Summary:        Test utilities for OpenTelemetry Collector
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector
#!RemoteAsset:  sha256:d881d6111e89cbc26d7661a9e2e15d1111bf05897824b6042f4dbe52f10b3fd6
Source0:        https://github.com/open-telemetry/opentelemetry-collector/archive/refs/tags/internal/testutil/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/collector/internal/testutil) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
This package provides the Go library go.opentelemetry.io/collector/internal/testutil.

%install
# The upstream module tag archive contains the whole collector repository, so
# build this package from its module subdirectory. - HNO3Miracle
pushd internal/testutil
%buildsystem_golangmodules_install
popd

%check
pushd internal/testutil
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
