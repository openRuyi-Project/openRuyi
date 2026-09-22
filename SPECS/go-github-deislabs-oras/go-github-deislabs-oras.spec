# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           oras
%define go_import_path  github.com/deislabs/oras
# These package tests start a complete Docker Registry and pull in its legacy
# observability stack. cmd/oras still compiles both production packages.
%define go_test_exclude %{go_import_path}/pkg/auth/docker %{go_import_path}/pkg/oras

Name:           go-github-deislabs-oras
Version:        0.8.1
Release:        %autorelease
Summary:        Registries are evolving as Cloud Native Artifact Stores
License:        MIT
URL:            https://github.com/deislabs/oras
VCS:            git:https://github.com/deislabs/oras.git
#!RemoteAsset:  sha256:4c2482aa2b804c8deaa0a355977960593a10c23b60438575fa239e99d44d4b96
Source0:        https://github.com/deislabs/oras/archive/v0.8.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n oras-0.8.1
# Current containerd rejects the suite's second commit on a closed writer.
BuildOption(check):  -skip '^TestContentTestSuite$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/containerd)
BuildRequires:  go(github.com/docker/cli)
BuildRequires:  go(github.com/docker/distribution)
BuildRequires:  go(github.com/docker/docker)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/phayes/freeport)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sync)

Provides:       go(github.com/deislabs/oras) = %{version}

Requires:       go(github.com/containerd/containerd)
Requires:       go(github.com/docker/cli)
Requires:       go(github.com/docker/docker)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/spf13/cobra)
Requires:       go(golang.org/x/sync)

%description
This package provides the github.com/deislabs/oras Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
