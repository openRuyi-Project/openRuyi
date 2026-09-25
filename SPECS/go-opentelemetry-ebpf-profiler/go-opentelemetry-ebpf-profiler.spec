# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ebpf-profiler
%define go_import_path  go.opentelemetry.io/ebpf-profiler
# Coredump tests download external fixtures. Two ELF test packages need
# generated binaries absent from release archives. internal/tools is a nested
# tool module that retains the repository's former GitHub import path.
%define go_test_exclude %{shrink:
    %{go_import_path}/internal/tools
    %{go_import_path}/libpf/pfelf
    %{go_import_path}/nativeunwind/elfunwindinfo
    %{go_import_path}/tools/coredump
}

Name:           go-opentelemetry-ebpf-profiler
Version:        0.0.202622
Release:        %autorelease
Summary:        Whole-system eBPF profiler for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-ebpf-profiler
#!RemoteAsset:  sha256:9549be5adedc35485da04314a46ff9e24e59284ba8e19499bd19b1df8a7bd466
Source0:        https://github.com/open-telemetry/opentelemetry-ebpf-profiler/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cilium/ebpf)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/elastic/go-freelru)
BuildRequires:  go(github.com/elastic/go-perf)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/mdlayher/kobject)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(github.com/mdlayher/socket)
BuildRequires:  go(github.com/minio/sha256-simd)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/open-telemetry/sig-profiling)
BuildRequires:  go(github.com/peterbourgon/ff/v3)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/proto)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/arch)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/cilium/ebpf)
Requires:       go(github.com/elastic/go-freelru)
Requires:       go(github.com/elastic/go-perf)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/mdlayher/kobject)
Requires:       go(github.com/minio/sha256-simd)
Requires:       go(github.com/open-telemetry/sig-profiling)
Requires:       go(github.com/peterbourgon/ff/v3)
Requires:       go(github.com/zeebo/xxh3)
Requires:       go(go.opentelemetry.io/collector)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/arch)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
The OpenTelemetry eBPF profiler provides low-overhead, whole-system profiling
for native and managed-language workloads on Linux.

%check -a
for pkg in \
    %{go_import_path}/libpf/pfelf \
    %{go_import_path}/nativeunwind/elfunwindinfo \
    %{go_import_path}/tools/coredump; do
    go test -c -o /dev/null "${pkg}"
done

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
