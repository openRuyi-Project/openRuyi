# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           containerd
%define go_import_path  github.com/containerd/containerd
%define go_test_include %{shrink:
    %{go_import_path}/archive/compression
    %{go_import_path}/content
    %{go_import_path}/content/local
    %{go_import_path}/errdefs
    %{go_import_path}/filters
    %{go_import_path}/images
    %{go_import_path}/labels
    %{go_import_path}/log
    %{go_import_path}/platforms
    %{go_import_path}/reference
    %{go_import_path}/remotes
    %{go_import_path}/remotes/docker
    %{go_import_path}/remotes/docker/schema1
    %{go_import_path}/sys
    %{go_import_path}/version
}

Name:           go-github-containerd-containerd
Version:        1.4.1
Release:        %autorelease
Summary:        Go library for containerd
License:        Apache-2.0
URL:            https://github.com/containerd/containerd
VCS:            git:https://github.com/containerd/containerd.git
#!RemoteAsset:  sha256:d410b8efc94e4124990f01de7107223971be8c9258fc651decf9e0ba648485b5
Source0:        https://github.com/containerd/containerd/archive/v1.4.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n containerd-1.4.1
BuildOption(check):  -vet=off -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/continuity)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(gotest.tools/v3)

Provides:       go(github.com/containerd/containerd) = %{version}

Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/grpc)

%description
This package provides the github.com/containerd/containerd Go module source.

%prep -a
# Go module providers must not leak a nested vendor tree into other builds.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
