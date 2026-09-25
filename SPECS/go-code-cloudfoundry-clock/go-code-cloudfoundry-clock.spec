# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clock
%define go_import_path  code.cloudfoundry.org/clock

Name:           go-code-cloudfoundry-clock
Version:        1.84.0
Release:        %autorelease
Summary:        Injectable clock interface for Go
License:        Apache-2.0
URL:            https://github.com/cloudfoundry/clock
#!RemoteAsset:  sha256:0d48504f1b94e23311589e42f445abca0893289f785c5647b71f073f1b39a853
Source0:        https://github.com/cloudfoundry/clock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/tedsuo/ifrit)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}

%description
Clock provides an injectable time interface and real and fake clock
implementations for deterministic Go tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
