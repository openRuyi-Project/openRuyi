# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           consumertest
%define go_import_path  go.opentelemetry.io/collector/consumer/consumertest

Name:           go-opentelemetry-collector-consumer-consumertest
Version:        0.152.0
Release:        %autorelease
Summary:        Go library for go.opentelemetry.io/collector/consumer/consumertest
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector
#!RemoteAsset:  sha256:96b37818813fd2d19dbb436cd345ec69976ec2cef2aae1aacc4efdc5ec514907
Source0:        https://github.com/open-telemetry/opentelemetry-collector/archive/refs/tags/consumer/consumertest/v0.152.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-collector-consumer-consumertest-v0.152.0/consumer/consumertest
# The import path is a Go module below the repository root; keep %check scoped
# to this module so GOPATH-mode tests do not scan sibling modules from the archive.
%define go_test_include %{go_import_path}

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/internal)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/xconsumer)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/plog)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/pmetric)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/pprofile)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/ptrace)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/testdata)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/collector/consumer/consumertest) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opentelemetry.io/collector/consumer)
Requires:       go(go.opentelemetry.io/collector/consumer/internal)
Requires:       go(go.opentelemetry.io/collector/consumer/xconsumer)
Requires:       go(go.opentelemetry.io/collector/featuregate)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/collector/pdata/plog)
Requires:       go(go.opentelemetry.io/collector/pdata/pmetric)
Requires:       go(go.opentelemetry.io/collector/pdata/pprofile)
Requires:       go(go.opentelemetry.io/collector/pdata/ptrace)
Requires:       go(go.opentelemetry.io/collector/pdata/testdata)
Requires:       go(go.uber.org/goleak)
Requires:       go(go.uber.org/multierr)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides the Go library go.opentelemetry.io/collector/consumer/consumertest.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
