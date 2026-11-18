# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ginkgolinter
%define go_import_path  github.com/nunnatsa/ginkgolinter

Name:           go-github-nunnatsa-ginkgolinter
Version:        0.24.0
Release:        %autorelease
Summary:        Go analyzer for Ginkgo and Gomega test assertions
License:        MIT
URL:            https://github.com/nunnatsa/ginkgolinter
#!RemoteAsset:  sha256:a11764ea98a5acd75c53d8c2b5546907aec7495245bab1a8479bf1084034f0eb
Source0:        https://github.com/nunnatsa/ginkgolinter/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/go-toolsmith/astcopy)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/nunnatsa/ginkgolinter) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/cmd/ginkgolinter/cli) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/config) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/expression) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/expression/actual) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/expression/matcher) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/expression/value) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/formatter) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/ginkgohandler) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/ginkgoinfo) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/gomegahandler) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/gomegainfo) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/intervals) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/reports) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/reverseassertion) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/rules) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/internal/typecheck) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/linter) = %{version}
Provides:       go(github.com/nunnatsa/ginkgolinter/version) = %{version}

Requires:       go(github.com/go-toolsmith/astcopy)
Requires:       go(golang.org/x/tools)

%description
Go analyzer for Ginkgo and Gomega test assertions.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n ginkgolinter-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/nunnatsa/ginkgolinter

%changelog
%autochangelog
