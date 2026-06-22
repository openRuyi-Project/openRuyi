# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           featuregate
%define go_import_path  go.opentelemetry.io/collector/featuregate
# Keep %check scoped to this module so GOPATH-mode tests do not scan sibling
# modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-opentelemetry-collector-featuregate
Version:        1.58.0
Release:        %autorelease
Summary:        Feature gate module for OpenTelemetry Collector
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector
#!RemoteAsset:  sha256:3c5995207bd322d28cbd82643e8856fb20ee3fb63a959b7c048f8d11b088aa1f
Source0:        https://github.com/open-telemetry/opentelemetry-collector/archive/refs/tags/featuregate/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/collector/featuregate) = %{version}

Requires:       go(github.com/hashicorp/go-version)
Requires:       go(go.uber.org/multierr)

%description
This package provides the Go library go.opentelemetry.io/collector/featuregate.

%install
# The upstream module tag archive contains the whole collector repository, so
# build this package from its module subdirectory. - HNO3Miracle
pushd featuregate
%buildsystem_golangmodules_install
popd

%check
pushd featuregate
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
