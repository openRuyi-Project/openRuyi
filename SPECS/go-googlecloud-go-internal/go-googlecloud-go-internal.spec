# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           internal
%define go_import_path  cloud.google.com/go/internal

Name:           go-googlecloud-go-internal
Version:        14617
Release:        %autorelease
Summary:        Internal support packages for Google Cloud Go clients
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:0c768debe4b6f6cb1328b5ee5ff9c761036229ec76dc1b476fcb66680bbdbafa
Source0:        https://github.com/googleapis/google-cloud-go/archive/release-%{version}.tar.gz#/%{_name}-release-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Package only the internal helper subtrees actually imported by split
# google-cloud-go modules. Building the monorepo root pulls a broad dependency
# cycle; these leaf helpers keep iam and translate checks/builds resolvable. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(google.golang.org/api/googleapi)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(cloud.google.com/go/internal) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/api/googleapi)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides internal helper packages used by split Google Cloud Go
client modules.

%install
install -dm0755 %{buildroot}%{go_sys_gopath}/%{go_import_path}
cp -a internal/*.go %{buildroot}%{go_sys_gopath}/%{go_import_path}/
for dir in internal/optional internal/testutil internal/trace internal/uid internal/version; do
    install -dm0755 %{buildroot}%{go_sys_gopath}/cloud.google.com/go/$dir
    cp -a $dir/*.go %{buildroot}%{go_sys_gopath}/cloud.google.com/go/$dir/
done

%check
mkdir -p _build/src/cloud.google.com/go/internal
cp -a internal/*.go _build/src/cloud.google.com/go/internal/
cp -a internal/optional _build/src/cloud.google.com/go/internal/
cp -a internal/testutil _build/src/cloud.google.com/go/internal/
cp -a internal/trace _build/src/cloud.google.com/go/internal/
cp -a internal/uid _build/src/cloud.google.com/go/internal/
cp -a internal/version _build/src/cloud.google.com/go/internal/
GO111MODULE=off GOPATH="$PWD/_build:%{_datadir}/gocode" go test -v \
    cloud.google.com/go/internal \
    cloud.google.com/go/internal/optional \
    cloud.google.com/go/internal/testutil \
    cloud.google.com/go/internal/trace \
    cloud.google.com/go/internal/uid \
    cloud.google.com/go/internal/version

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
