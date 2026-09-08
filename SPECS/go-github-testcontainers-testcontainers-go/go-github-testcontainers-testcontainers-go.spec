# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testcontainers-go
%define go_import_path  github.com/testcontainers/testcontainers-go
# Integration packages require a container runtime unavailable in OBS workers.
%define go_test_exclude %{go_import_path} %{go_import_path}/network %{go_import_path}/wait
# The remaining patterns are independently versioned modules in this repository.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/examples*
    %{go_import_path}/modulegen*
    %{go_import_path}/modules*
    %{go_import_path}/usage-metrics*
    %{go_import_path}/wait/testdata/http*
}

Name:           go-github-testcontainers-testcontainers-go
Version:        0.44.0
Release:        %autorelease
Summary:        Container-based integration testing for Go
License:        MIT
URL:            https://github.com/testcontainers/testcontainers-go
#!RemoteAsset:  sha256:63824450478790f6fc5dc38fa6189093ba8bae8e493335d7929482dd213f3324
Source0:        https://github.com/testcontainers/testcontainers-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use the numeric mount type's correct formatting verb.
Patch2000:      2000-Fix-mount-type-format-verb.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/Azure/go-ansiterm)
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/containerd/platforms)
BuildRequires:  go(github.com/cpuguy83/dockercfg)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/docker/go-connections)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/ebitengine/purego)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/moby/docker-image-spec)
BuildRequires:  go(github.com/moby/go-archive)
BuildRequires:  go(github.com/moby/moby/api)
BuildRequires:  go(github.com/moby/moby/client)
BuildRequires:  go(github.com/moby/patternmatcher)
BuildRequires:  go(github.com/moby/sys/sequential)
BuildRequires:  go(github.com/moby/sys/user)
BuildRequires:  go(github.com/moby/sys/userns)
BuildRequires:  go(github.com/moby/term)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/shirou/gopsutil/v4)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(dario.cat/mergo)
Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/containerd/errdefs)
Requires:       go(github.com/containerd/platforms)
Requires:       go(github.com/cpuguy83/dockercfg)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/magiconair/properties)
Requires:       go(github.com/moby/go-archive)
Requires:       go(github.com/moby/moby/api)
Requires:       go(github.com/moby/moby/client)
Requires:       go(github.com/moby/patternmatcher)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/shirou/gopsutil/v4)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/crypto)

%description
Testcontainers for Go creates and manages disposable containers for integration
tests through Docker-compatible container runtimes.

%check
export GODEBUG=asynctimerchan=0
%buildsystem_golangmodules_check
go test -run '^$' \
    %{go_import_path} \
    %{go_import_path}/network \
    %{go_import_path}/wait
go list -e -f '{{.ImportPath}}' ./examples/... | \
    grep -v '^%{go_import_path}/examples/nginx$' | \
    xargs go test -run '^$'

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/examples/nginx
%exclude %{go_sys_gopath}/%{go_import_path}/modulegen
%exclude %{go_sys_gopath}/%{go_import_path}/modules
%exclude %{go_sys_gopath}/%{go_import_path}/usage-metrics
%exclude %{go_sys_gopath}/%{go_import_path}/wait/testdata/http

%changelog
%autochangelog
