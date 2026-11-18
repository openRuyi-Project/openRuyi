# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           loggercheck
%define go_import_path  github.com/timonwong/loggercheck

Name:           go-github-timonwong-loggercheck
Version:        0.13.1
Release:        %autorelease
Summary:        Go analyzer for structured logging key and value pairs
License:        MIT
URL:            https://github.com/timonwong/loggercheck
#!RemoteAsset:  sha256:39930e729499d5000247eba0a927c6ed7d08e92c2490857929dc9c1653cecdd0
Source0:        https://github.com/timonwong/loggercheck/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-kit/log)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(k8s.io/klog/v2)

Provides:       go(github.com/timonwong/loggercheck) = %{version}
Provides:       go(github.com/timonwong/loggercheck/internal/checkers) = %{version}
Provides:       go(github.com/timonwong/loggercheck/internal/checkers/printf) = %{version}
Provides:       go(github.com/timonwong/loggercheck/internal/nilness) = %{version}
Provides:       go(github.com/timonwong/loggercheck/internal/rules) = %{version}
Provides:       go(github.com/timonwong/loggercheck/internal/sets) = %{version}
Provides:       go(github.com/timonwong/loggercheck/internal/stringutil) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for structured logging key and value pairs.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n loggercheck-%{version}

%check
# analysistest creates an isolated GOPATH under testdata/src; expose packaged
# dependency trees there so fixture imports resolve without modifying fixtures.
ln -s %{_datadir}/gocode/src/github.com testdata/src/github.com
ln -s %{_datadir}/gocode/src/go.uber.org testdata/src/go.uber.org
ln -s %{_datadir}/gocode/src/k8s.io testdata/src/k8s.io
%buildsystem_golangmodules_check

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/timonwong/loggercheck

%changelog
%autochangelog
