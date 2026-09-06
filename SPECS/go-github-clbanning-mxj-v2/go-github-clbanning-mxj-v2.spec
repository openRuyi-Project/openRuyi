# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mxj
%define go_import_path  github.com/clbanning/mxj/v2
# The examples directory contains multiple standalone main packages.
%define go_test_exclude %{go_import_path}/examples

Name:           go-github-clbanning-mxj-v2
Version:        2.7.0
Release:        %autorelease
Summary:        XML and JSON map utilities for Go
License:        MIT
URL:            https://github.com/clbanning/mxj
#!RemoteAsset:  sha256:5c6099ffe102dcd4b77af26fba00db5769846df2890d75c94cf838eb94b9a963
Source0:        https://github.com/clbanning/mxj/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/clbanning/mxj)
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/clbanning/mxj)

%description
Package mxj decodes and encodes XML and JSON values as Go maps and provides
helpers for querying and modifying map values by key paths.

%check
export GO111MODULE=off
_check_gopath=%{_builddir}/%{name}-check
install -d ${_check_gopath}/src/%{go_import_path}
cp -a . ${_check_gopath}/src/%{go_import_path}
pushd ${_check_gopath}/src/%{go_import_path}
# Search the system GOPATH first so the v2 compatibility packages can import
# the separately packaged unversioned github.com/clbanning/mxj module.
export GOPATH=%{_datadir}/gocode:${_check_gopath}
go test -v -vet=off \
    $(go list ./... | grep -vx '%{go_test_exclude}')
popd

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
