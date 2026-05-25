# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-metrics
%define go_import_path  github.com/hashicorp/go-metrics
%define go_compat_import_path  github.com/armon/go-metrics
# Circonus, Prometheus and local socket sink tests are incompatible with
# packaged dependency versions or the OBS build environment. - HNO3Miracle
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/circonus
    %{go_import_path}/datadog
    %{go_import_path}/prometheus
}

Name:           go-github-armon-go-metrics
Version:        0.5.4
Release:        %autorelease
Summary:        Metrics instrumentation library for Go
License:        MIT
URL:            https://github.com/armon/go-metrics
#!RemoteAsset:  sha256:f7646f26c37d299018248f4ee67cf464396b9bec2192389a85c7826575b64560
Source0:        https://github.com/armon/go-metrics/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Without this patch, the package does not compile against packaged
# go-immutable-radix v2: iradix.Tree is generic and Get already returns bool,
# so the old non-generic tree field and type assertion fail. - HNO3Miracle
Patch2000:      2000-fix-go-immutable-radix-v2-compatibility.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/datadog-go)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/circonus-labs/circonus-gometrics)
BuildRequires:  go(github.com/circonus-labs/circonusllhist)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/pascaldekloe/goe)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/tv42/httpunix)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/armon/go-metrics) = %{version}
Provides:       go(github.com/hashicorp/go-metrics) = %{version}

Requires:       go(github.com/DataDog/datadog-go)
Requires:       go(github.com/beorn7/perks)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/circonus-labs/circonus-gometrics)
Requires:       go(github.com/circonus-labs/circonusllhist)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-immutable-radix)
Requires:       go(github.com/hashicorp/go-retryablehttp)
Requires:       go(github.com/hashicorp/golang-lru)
Requires:       go(github.com/matttproud/golang_protobuf_extensions)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/tv42/httpunix)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description
This library provides a metrics package which can be used to instrument
code, expose application metrics, and profile runtime performance in a
flexible manner.

# Upstream v0.5.4 declares module github.com/hashicorp/go-metrics while the
# source archive still comes from github.com/armon/go-metrics. Install a
# compatibility copy for consumers that still import the old path.
%install -a
mkdir -p %{buildroot}%{go_sys_gopath}/$(dirname %{go_compat_import_path})
cp -a %{buildroot}%{go_sys_gopath}/%{go_import_path} \
      %{buildroot}%{go_sys_gopath}/%{go_compat_import_path}

# The default golangmodules check only copies %{go_import_path} into the
# temporary GOPATH. This module's compat packages import the old
# github.com/armon/go-metrics path, so copy both paths before running tests.
# Run only the compat packages that do not need excluded sink packages or OBS
# local socket behavior; this mirrors go_test_exclude for the custom check.
# - HNO3Miracle
%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/$(dirname %{go_import_path})
rm -rf %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
mkdir -p %{_builddir}/go/src/$(dirname %{go_compat_import_path})
cp -a %{_builddir}/go/src/%{go_import_path} \
      %{_builddir}/go/src/%{go_compat_import_path}
cd %{_builddir}/go/src/%{go_import_path}
go test -v \
    %{go_import_path}/compat/circonus \
    %{go_import_path}/compat/datadog \
    %{go_import_path}/compat/prometheus

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/%{go_compat_import_path}

%changelog
%autochangelog
