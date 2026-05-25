# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testutil
%define go_import_path  go.opentelemetry.io/collector/internal/testutil

Name:           go-opentelemetry-collector-internal-testutil
Version:        0.152.0
Release:        %autorelease
Summary:        Go library for go.opentelemetry.io/collector/internal/testutil
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector
#!RemoteAsset:  sha256:d881d6111e89cbc26d7661a9e2e15d1111bf05897824b6042f4dbe52f10b3fd6
Source0:        https://github.com/open-telemetry/opentelemetry-collector/archive/refs/tags/internal/testutil/v0.152.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-collector-internal-testutil-v0.152.0/internal/testutil
# The import path is a Go module below the repository root; keep %check scoped
# to this module so GOPATH-mode tests do not scan sibling modules from the archive.
%define go_test_include %{go_import_path}

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/collector/internal/testutil) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/kr/text)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.uber.org/goleak)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides the Go library go.opentelemetry.io/collector/internal/testutil.

%files
%doc README.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
