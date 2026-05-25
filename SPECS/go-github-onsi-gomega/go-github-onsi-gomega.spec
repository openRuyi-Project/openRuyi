# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gomega
%define go_import_path  github.com/onsi/gomega
# The upstream test suite is written with github.com/onsi/ginkgo/v2, while
# ginkgo itself needs gomega. Exclude gomega tests to break the packaging
# bootstrap cycle; ginkgo can run its own tests after gomega is available.
# - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}*

Name:           go-github-onsi-gomega
Version:        1.39.1
Release:        %autorelease
Summary:        Matcher and assertion helpers for Go tests
License:        MIT
URL:            https://github.com/onsi/gomega
#!RemoteAsset:  sha256:fe509b33154b7c69e9aa0c1546914a9fb0d04409aa01d55ffe91767ae11b3450
Source0:        https://github.com/onsi/gomega/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/onsi/gomega) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/net)
Requires:       go(google.golang.org/protobuf)

%description
Gomega provides matcher and assertion helpers for Go tests.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
