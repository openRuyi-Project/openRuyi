# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nri
%define go_import_path  github.com/containerd/nri
# TODO!
# runtime-tools/generate remains excluded: runtime-tools v0.9.0 exposes vendored
# runtime-spec types, while NRI uses the system runtime-spec package. Go treats
# these identically named types as incompatible import paths in GOPATH mode.
%define go_test_exclude %{shrink:
    %{go_import_path}/pkg/runtime-tools/generate
    %{go_import_path}/plugins/device-injector
    %{go_import_path}/plugins/differ
    %{go_import_path}/plugins/hook-injector
    %{go_import_path}/plugins/logger
    %{go_import_path}/plugins/network-device-injector
    %{go_import_path}/plugins/template
    %{go_import_path}/plugins/ulimit-adjuster
    %{go_import_path}/plugins/v010-adapter
    %{go_import_path}/plugins/wasm
}

Name:           go-github-containerd-nri
Version:        0.12.0
Release:        %autorelease
Summary:        Node Resource Interface
License:        Apache-2.0
URL:            https://github.com/containerd/nri
#!RemoteAsset:  sha256:6f0d3af7ba2420cbcbe72e468833bc146f359942810e13aaaf86939a4ca53991
Source0:        https://github.com/containerd/nri/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/brianvoe/gofakeit/v7)
BuildRequires:  go(github.com/containerd/ttrpc)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/knqyf263/go-plugin) = 0.9.0
BuildRequires:  go(github.com/moby/sys/mountinfo)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tetratelabs/wazero)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(github.com/containerd/cgroups)
BuildRequires:  go(github.com/opencontainers/runtime-tools/generate)

Provides:       go(github.com/containerd/nri) = %{version}

Requires:       go
Requires:       go-rpm-macros
Requires:       go(github.com/brianvoe/gofakeit/v7)
Requires:       go(github.com/containerd/ttrpc)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/knqyf263/go-plugin) = 0.9.0
Requires:       go(github.com/moby/sys/mountinfo)
Requires:       go(github.com/onsi/ginkgo/v2)
Requires:       go(github.com/onsi/gomega)
Requires:       go(github.com/opencontainers/runtime-spec)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tetratelabs/wazero)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)

%description
NRI allows plugging domain- or vendor-specific custom logic
into OCI- compatible runtimes. This logic can make controlled
changes to containers or perform extra actions outside the
scope of OCI at certain points in a containers lifecycle.
This can be used, for instance, for improved allocation and
management of devices and other container resources.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
