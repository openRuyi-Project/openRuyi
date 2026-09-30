# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testing
%define go_import_path  github.com/golang-plus/testing

Name:           go-github-golang-plus-testing
Version:        1.0.0
Release:        %autorelease
Summary:        Assertion helpers for Go tests
License:        Apache-2.0
URL:            https://github.com/golang-plus/testing
#!RemoteAsset:  sha256:12827e852df2744c398676ed6717c875ec615318575e163b34bea6c9047aa1e8
Source0:        https://github.com/golang-plus/testing/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# Upstream added the license after v1.0.0.
# https://github.com/golang-plus/testing/blob/50ad5c5dd55d121bf18b269819254dc22817df9a/LICENSE
Source1:        LICENSE
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golang-plus/testing) = %{version}

%description
Assertion helpers for Go tests.

%prep -a
cp %{SOURCE1} LICENSE

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
