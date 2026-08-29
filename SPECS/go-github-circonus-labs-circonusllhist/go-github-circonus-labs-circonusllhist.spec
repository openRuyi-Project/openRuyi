# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           circonusllhist
%define go_import_path  github.com/circonus-labs/circonusllhist

Name:           go-github-circonus-labs-circonusllhist
Version:        0.4.1
Release:        %autorelease
Summary:        Go implementation of OpenHistogram log-linear histograms
License:        Apache-2.0
URL:            https://github.com/circonus-labs/circonusllhist
#!RemoteAsset:  sha256:ec28fd8dc0f033cdfd5538d68f2b69e7f9989bc0d4cd2c6ae4509fdf5b8a26b3
Source0:        https://github.com/circonus-labs/circonusllhist/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/circonus-labs/circonusllhist) = %{version}

%description
This package provides a Go implementation of OpenHistogram log-linear
histograms.

%install -a
# The repository moved from github.com/openhistogram/circonusllhist to
# github.com/circonus-labs/circonusllhist, but this release still tests and
# supports the legacy import path. The custom install/check keeps both import
# paths available because the default golangmodules macros only prepare the
# primary %{go_import_path}. - HNO3Miracle
install -d %{buildroot}%{go_sys_gopath}/github.com/openhistogram
cp -a %{buildroot}%{go_sys_gopath}/%{go_import_path} \
    %{buildroot}%{go_sys_gopath}/github.com/openhistogram/circonusllhist

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d %{_builddir}/go/src/github.com/circonus-labs
cp -a . %{_builddir}/go/src/%{go_import_path}
install -d %{_builddir}/go/src/github.com/openhistogram
cp -a . %{_builddir}/go/src/github.com/openhistogram/circonusllhist
cd %{_builddir}/go/src/%{go_import_path}
go test -v %{go_import_path}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/github.com/openhistogram/circonusllhist

%changelog
%autochangelog
