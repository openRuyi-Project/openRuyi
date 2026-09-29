# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uuid
%define go_import_path  github.com/golang-plus/uuid

Name:           go-github-golang-plus-uuid
Version:        1.0.0
Release:        %autorelease
Summary:        Go library for uuid
License:        Apache-2.0
URL:            https://github.com/golang-plus/uuid
VCS:            git:https://github.com/golang-plus/uuid.git
#!RemoteAsset:  sha256:6e0f90573f8c47eef05f908a00d39763d572f9fde38f871e803b73b32c445f50
Source0:        https://github.com/golang-plus/uuid/archive/v1.0.0.tar.gz#/%{_name}-%{version}.tar.gz
# v1.0.0 predates the upstream commit that added the Apache-2.0 text.
#!RemoteAsset:  sha256:3dc696a0da74a7dbf4d802887450d1b2487a264ae14dfc90595b012818c1caa8
Source1:        https://raw.githubusercontent.com/golang-plus/uuid/47d03abc30964f35b881c5a77f6c3087385a94fe/LICENSE
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n uuid-1.0.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang-plus/errors)
BuildRequires:  go(github.com/golang-plus/testing)

Provides:       go(github.com/golang-plus/uuid) = %{version}

Requires:       go(github.com/golang-plus/errors)

%description
This package provides the github.com/golang-plus/uuid Go module source.

%prep -a
cp %{SOURCE1} LICENSE

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
