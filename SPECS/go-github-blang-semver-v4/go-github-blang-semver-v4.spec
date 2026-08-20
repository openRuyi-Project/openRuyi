# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           semver
%define go_import_path  github.com/blang/semver/v4
%define go_source_subdir v4

Name:           go-github-blang-semver-v4
Version:        4.0.0
Release:        %autorelease
Summary:        Semantic Versioning library for Go
License:        MIT
URL:            https://github.com/blang/semver
#!RemoteAsset:  sha256:873e979323df6060cb4f843bc920f07fa59c05002359bf5d4a3311c8911f6640
Source0:        https://github.com/blang/semver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/blang/semver/v4) = %{version}

%description
Semantic Versioning library for Go. It implements version 2.0.0 of the
Semantic Versioning specification.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/$(dirname %{go_import_path})
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
go test -vet=off -v ./...
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
