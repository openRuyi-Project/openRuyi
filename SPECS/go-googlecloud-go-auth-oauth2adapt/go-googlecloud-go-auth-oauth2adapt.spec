# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           oauth2adapt
%define go_import_path  cloud.google.com/go/auth/oauth2adapt
%define go_source_subdir auth/oauth2adapt

Name:           go-googlecloud-go-auth-oauth2adapt
Version:        0.2.8
Release:        %autorelease
Summary:        Go library for cloud.google.com/go/auth/oauth2adapt
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:55481ab06b21172f13e4c6862927873a90ca8eddf1faf936d481cc8b6ee70744
Source0:        https://github.com/googleapis/google-cloud-go/archive/refs/tags/auth/oauth2adapt/v0.2.8.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n google-cloud-go-auth-oauth2adapt-v0.2.8
# The explicit %%install/%%check sections below enter %%{go_source_subdir}; using
# BuildOption(prep): -n .../auth/oauth2adapt would copy the whole repository
# under the oauth2adapt import path because the GitHub archive still contains
# the top-level directory.

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go-rpm-macros

Provides:       go(cloud.google.com/go/auth/oauth2adapt) = %{version}

%description
This package provides the Go library cloud.google.com/go/auth/oauth2adapt.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
# oauth2adapt imports its parent module cloud.google.com/go/auth. Copy the
# installed parent tree into the first GOPATH entry before adding this submodule;
# otherwise the empty parent directory created for oauth2adapt shadows it.
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/cloud.google.com/go
rm -rf %{_builddir}/go/src/cloud.google.com/go/auth
cp -a %{_datadir}/gocode/src/cloud.google.com/go/auth %{_builddir}/go/src/cloud.google.com/go/auth
rm -rf %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
go test -v %{go_import_path}
popd

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
