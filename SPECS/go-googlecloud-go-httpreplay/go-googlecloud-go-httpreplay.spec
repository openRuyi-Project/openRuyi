# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpreplay
%define go_import_path  cloud.google.com/go/httpreplay
%define go_source_subdir httpreplay

Name:           go-googlecloud-go-httpreplay
Version:        1.62.2
Release:        %autorelease
Summary:        HTTP replay helpers for Google Cloud Go tests
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:38afa699c95151053154d1ab2605148a05768e41ade567c6dc15920562893a79
Source0:        https://github.com/googleapis/google-cloud-go/archive/refs/tags/storage/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n google-cloud-go-storage-v%{version}
# httpreplay is not tagged as an independent module in this archive. Package
# only the source subtree needed by storage tests and keep sibling internal
# packages in the temporary GOPATH during %%check.

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/internal/testutil)
BuildRequires:  go(github.com/google/martian/v3)
BuildRequires:  go(google.golang.org/api/option)
BuildRequires:  go(google.golang.org/api/transport/http)
BuildRequires:  go-rpm-macros

Provides:       go(cloud.google.com/go/httpreplay) = %{version}
Provides:       go(cloud.google.com/go/httpreplay/internal/proxy) = %{version}

Requires:       go(cloud.google.com/go/internal/testutil)
Requires:       go(github.com/google/martian/v3)
Requires:       go(google.golang.org/api/option)
Requires:       go(google.golang.org/api/transport/http)

%description
This package provides HTTP record/replay helpers used by Google Cloud Go tests.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf "%{_builddir}/go/src/cloud.google.com/go"
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
cp -a ../internal "%{_builddir}/go/src/cloud.google.com/go/internal"
cd "%{_builddir}/go/src/%{go_import_path}"
# httpreplay_test.go imports cloud.google.com/go/storage for integration replay
# coverage; storage depends on this package, so keep only the local proxy tests
# here to avoid a test-only bootstrap cycle.
rm -f httpreplay_test.go
# cmd/httpr/integration_test.go imports cloud.google.com/go/storage; storage
# BuildRequires this package, so skip that command package to avoid the same
# bootstrap cycle while still running the local proxy tests.
go test -v $(go list -e -f '{{.ImportPath}}' ./... | grep -v '^cloud.google.com/go/httpreplay/cmd/httpr$')
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
