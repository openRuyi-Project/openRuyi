# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           client
%define go_import_path  go.etcd.io/etcd/client/v2

Name:           go-etcd-io-etcd-client-v2
Version:        2.305.33
Release:        %autorelease
Summary:        Version 2 etcd client library for Go
License:        Apache-2.0
URL:            https://github.com/etcd-io/etcd
#!RemoteAsset:  sha256:1c42bc255fc8e17a5c932b10045a8eefe91f3ab31e8f89d17c76bd92b78cccf5
Source0:        https://github.com/etcd-io/etcd/archive/refs/tags/client/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n etcd-client-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(go.etcd.io/etcd/api/v3)
BuildRequires:  go(go.etcd.io/etcd/client/pkg/v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(go.etcd.io/etcd/api/v3)
Requires:       go(go.etcd.io/etcd/client/pkg/v3)

%description
This package provides the version 2 etcd client library from the etcd source
repository.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -aL client/v2/. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
export GO111MODULE=off
export GOPATH="%{_builddir}/go:%{_datadir}/gocode"
install -d "%{_builddir}/go/src/%{go_import_path}"
cp -aL client/v2/. "%{_builddir}/go/src/%{go_import_path}/"
pushd "%{_builddir}/go/src/%{go_import_path}"
go test -v $(go list -e -f '{{.ImportPath}}' ./...)
popd

%files
%doc client/v2/README.md
%license client/v2/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
