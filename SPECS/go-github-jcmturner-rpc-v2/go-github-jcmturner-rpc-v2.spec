# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name            rpc
%define go_import_path   github.com/jcmturner/rpc/v2

Name:           go-github-jcmturner-rpc-v2
Version:        2.0.3
Release:        %autorelease
Summary:        Microsoft RPC and NDR implementation for Go
License:        Apache-2.0
URL:            https://github.com/jcmturner/rpc
#!RemoteAsset:  sha256:4bedb66a89dd261063d42e5f08d22eab3373ef529a78d72800f8727b62336ca3
Source0:        https://github.com/jcmturner/rpc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/jcmturner/rpc/v2) = %{version}

Requires:       go(golang.org/x/net)

%description
Rpc implements Microsoft RPC data types and Network Data Representation
encoding for Go.

%install
pushd v2
%buildsystem_golangmodules_install
popd

%check
pushd v2
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
