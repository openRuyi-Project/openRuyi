# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errors
%define go_import_path  github.com/golang-plus/errors

Name:           go-github-golang-plus-errors
Version:        1.0.0
Release:        %autorelease
Summary:        Go library for errors
License:        Apache-2.0
URL:            https://github.com/golang-plus/errors
VCS:            git:https://github.com/golang-plus/errors.git
#!RemoteAsset:  sha256:5452d8c1efc5105c0158e76c4b1656bc9c1e2778dbdc929405f29a62006874f4
Source0:        https://github.com/golang-plus/errors/archive/v1.0.0.tar.gz#/%{_name}-%{version}.tar.gz
# v1.0.0 predates the upstream commit that added the Apache-2.0 text.
#!RemoteAsset:  sha256:3dc696a0da74a7dbf4d802887450d1b2487a264ae14dfc90595b012818c1caa8
Source1:        https://raw.githubusercontent.com/golang-plus/errors/ba223c001a0652d97128ab4f47efee9d7529560b/LICENSE
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n errors-1.0.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golang-plus/errors) = %{version}

%description
This package provides the github.com/golang-plus/errors Go module source.

%prep -a
cp %{SOURCE1} LICENSE

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
