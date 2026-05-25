# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gomega
%define go_import_path  github.com/onsi/gomega

Name:           go-github-onsi-gomega
Version:        1.39.1
Release:        %autorelease
Summary:        Go library for github.com/onsi/gomega
License:        MIT
URL:            https://github.com/onsi/gomega
#!RemoteAsset:  sha256:fe509b33154b7c69e9aa0c1546914a9fb0d04409aa01d55ffe91767ae11b3450
Source0:        https://github.com/onsi/gomega/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gomega-1.39.1
# The upstream test suite is written with github.com/onsi/ginkgo/v2, while
# ginkgo itself needs gomega. Exclude gomega tests to break the packaging
# bootstrap cycle; ginkgo can run its own tests after gomega is available.
%define go_test_exclude_glob %{go_import_path}*

BuildRequires:  go
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/onsi/gomega) = %{version}
Provides:       go(github.com/onsi/gomega/format) = %{version}
Provides:       go(github.com/onsi/gomega/gbytes) = %{version}
Provides:       go(github.com/onsi/gomega/gcustom) = %{version}
Provides:       go(github.com/onsi/gomega/gexec) = %{version}
Provides:       go(github.com/onsi/gomega/ghttp) = %{version}
Provides:       go(github.com/onsi/gomega/ghttp/protobuf) = %{version}
Provides:       go(github.com/onsi/gomega/gleak) = %{version}
Provides:       go(github.com/onsi/gomega/gleak/goroutine) = %{version}
Provides:       go(github.com/onsi/gomega/gmeasure) = %{version}
Provides:       go(github.com/onsi/gomega/gmeasure/table) = %{version}
Provides:       go(github.com/onsi/gomega/gstruct) = %{version}
Provides:       go(github.com/onsi/gomega/gstruct/errors) = %{version}
Provides:       go(github.com/onsi/gomega/internal) = %{version}
Provides:       go(github.com/onsi/gomega/internal/gutil) = %{version}
Provides:       go(github.com/onsi/gomega/internal/testingtsupport) = %{version}
Provides:       go(github.com/onsi/gomega/matchers) = %{version}
Provides:       go(github.com/onsi/gomega/matchers/internal/miter) = %{version}
Provides:       go(github.com/onsi/gomega/matchers/support/goraph/bipartitegraph) = %{version}
Provides:       go(github.com/onsi/gomega/matchers/support/goraph/edge) = %{version}
Provides:       go(github.com/onsi/gomega/matchers/support/goraph/node) = %{version}
Provides:       go(github.com/onsi/gomega/matchers/support/goraph/util) = %{version}
Provides:       go(github.com/onsi/gomega/types) = %{version}

Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-task/slim-sprig/v3)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/Masterminds/semver/v3)
Requires:       go(go.uber.org/automaxprocs)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/tools)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library github.com/onsi/gomega.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
