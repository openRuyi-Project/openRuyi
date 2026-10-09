# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           consumer
%define go_import_path  go.opentelemetry.io/collector/consumer
# Keep %check scoped to this module so GOPATH-mode tests do not scan sibling
# modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-opentelemetry-collector-consumer
Version:        1.67.0
Release:        %autorelease
Summary:        Consumer APIs for OpenTelemetry Collector
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector
#!RemoteAsset:  sha256:ac3f551ea4c5bc1a190a011b8733db31ed7d7f06400cc56db0a9765552c88c0f
Source0:        https://github.com/open-telemetry/opentelemetry-collector/archive/refs/tags/consumer/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/collector/consumer) = %{version}

Requires:       go(go.opentelemetry.io/collector/pdata)

%description
This package provides the consumer module used by OpenTelemetry Collector.

%install
# The upstream module tag archive contains the whole collector repository, so
# build this package from its module subdirectory. - HNO3Miracle
pushd consumer
%buildsystem_golangmodules_install
popd

%check
pushd consumer
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%exclude %{go_sys_gopath}/%{go_import_path}/consumertest
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
