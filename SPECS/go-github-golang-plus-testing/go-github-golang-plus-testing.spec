# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testing
%define go_import_path  github.com/golang-plus/testing

Name:           go-github-golang-plus-testing
Version:        1.0.0
Release:        %autorelease
Summary:        Go testing helper library
License:        Apache-2.0
URL:            https://github.com/golang-plus/testing
VCS:            git:https://github.com/golang-plus/testing.git
#!RemoteAsset:  sha256:12827e852df2744c398676ed6717c875ec615318575e163b34bea6c9047aa1e8
Source0:        https://github.com/golang-plus/testing/archive/v1.0.0.tar.gz#/%{_name}-%{version}.tar.gz
# v1.0.0 predates the upstream commit that added the Apache-2.0 text.
#!RemoteAsset:  sha256:3dc696a0da74a7dbf4d802887450d1b2487a264ae14dfc90595b012818c1caa8
Source1:        https://raw.githubusercontent.com/golang-plus/testing/50ad5c5dd55d121bf18b269819254dc22817df9a/LICENSE
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n testing-1.0.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golang-plus/testing) = %{version}

%description
This package provides the github.com/golang-plus/testing Go module source.

%prep -a
cp %{SOURCE1} LICENSE

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
