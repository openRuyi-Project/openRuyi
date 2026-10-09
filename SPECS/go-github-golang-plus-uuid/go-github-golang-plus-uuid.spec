# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uuid
%define go_import_path  github.com/golang-plus/uuid

Name:           go-github-golang-plus-uuid
Version:        1.0.0
Release:        %autorelease
Summary:        UUID generation and parsing library for Go
License:        Apache-2.0
URL:            https://github.com/golang-plus/uuid
#!RemoteAsset:  sha256:6e0f90573f8c47eef05f908a00d39763d572f9fde38f871e803b73b32c445f50
Source0:        https://github.com/golang-plus/uuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# Upstream added the license after v1.0.0.
# https://github.com/golang-plus/uuid/blob/abc8f6f4d9f8ee48848030dba1eb233bc8b4c4fe/LICENSE
Source1:        LICENSE
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang-plus/errors)
BuildRequires:  go(github.com/golang-plus/testing)

Provides:       go(github.com/golang-plus/uuid) = %{version}

Requires:       go(github.com/golang-plus/errors)

%description
UUID generation and parsing library for Go.

%prep -a
cp %{SOURCE1} LICENSE

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
