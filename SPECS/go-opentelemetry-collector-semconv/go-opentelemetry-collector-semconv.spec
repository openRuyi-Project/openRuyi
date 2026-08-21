# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-collector
%define go_import_path  go.opentelemetry.io/collector/semconv

Name:           go-opentelemetry-collector-semconv
Version:        0.128.0
Release:        %autorelease
Summary:        Deprecated OpenTelemetry Collector semantic conventions
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector
#!RemoteAsset:  sha256:6fa273689dd67332591cba868fa7401c30615e24fbf5cd31b5334fa5f661175f
Source0:        https://github.com/open-telemetry/opentelemetry-collector/archive/refs/tags/semconv/v%{version}.tar.gz#/%{_name}-semconv-v%{version}.tar.gz
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
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides the deprecated OpenTelemetry Collector semantic
conventions module for software that has not migrated to the OpenTelemetry Go
semantic conventions.

%install
pushd semconv
%buildsystem_golangmodules_install
popd

%check
pushd semconv
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
