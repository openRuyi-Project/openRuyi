# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           processor
%define go_import_path  go.opentelemetry.io/collector/processor
# Keep %check scoped to this module so GOPATH-mode tests do not scan sibling
# modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-opentelemetry-collector-processor
Version:        1.58.0
Release:        %autorelease
Summary:        Processor APIs for OpenTelemetry Collector
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector
#!RemoteAsset:  sha256:07bd1e20ee2c5bbfc0a368dd7f114da35cabb6c937d58f557550056878bb6453
Source0:        https://github.com/open-telemetry/opentelemetry-collector/archive/refs/tags/processor/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumertest)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/internal/componentalias)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/pipeline)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/collector/processor) = %{version}

Requires:       go(go.opentelemetry.io/collector/component)
Requires:       go(go.opentelemetry.io/collector/consumer)
Requires:       go(go.opentelemetry.io/collector/internal/componentalias)
Requires:       go(go.opentelemetry.io/collector/pipeline)

%description
This package provides the processor module used by OpenTelemetry Collector.

%install
# The upstream module tag archive contains the whole collector repository, so
# build this package from its module subdirectory. - HNO3Miracle
pushd processor
%buildsystem_golangmodules_install
popd

%check
# processor imports collector/internal/componentalias from the same upstream
# module tree, so copy the parent collector tree into GOPATH before testing
# this module. - HNO3Miracle
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf "%{_builddir}/go/src/go.opentelemetry.io/collector"
mkdir -p "%{_builddir}/go/src/go.opentelemetry.io"
cp -a . "%{_builddir}/go/src/go.opentelemetry.io/collector"
go test -v %{go_test_include}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
