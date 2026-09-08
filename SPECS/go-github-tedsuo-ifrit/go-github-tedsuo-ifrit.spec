# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ifrit
%define go_import_path  github.com/tedsuo/ifrit
%define commit_id       94822c932811cb43f4bce35bb57ddd8186d61de8

Name:           go-github-tedsuo-ifrit
Version:        0+git20260818.94822c9
Release:        %autorelease
Summary:        Composable process model for Go
License:        MIT
URL:            https://github.com/tedsuo/ifrit
#!RemoteAsset:  sha256:85869c24b695494afc96781e4d5cc4184314524661d1a085436b4e522a51cc9c
Source0:        https://github.com/tedsuo/ifrit/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Locate test certificates correctly when GOPATH contains multiple entries.
Patch2000:      2000-test-handle-multiple-GOPATH-entries.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/examples)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/google/uuid)
Requires:       go(github.com/onsi/ginkgo/v2)
Requires:       go(github.com/onsi/gomega)
Requires:       go(google.golang.org/grpc)

%description
Ifrit defines a process model for composing, monitoring, and cleanly stopping
single-purpose units of work in Go programs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
