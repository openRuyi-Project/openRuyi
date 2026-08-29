# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-spiffe
%define go_import_path  github.com/spiffe/go-spiffe/v2
# go-google-grpc only needs go-spiffe's core SPIFFE ID and bundle packages.
# The workloadapi/spiffegrpc/spiffetls subtrees import grpc and create a source
# package cycle, so this core package removes those grpc-bound trees and skips
# packages whose tests import them. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/examples*
    %{go_import_path}/federation
    %{go_import_path}/internal/test/fakeworkloadapi*
    %{go_import_path}/proto/spiffe/workload*
    %{go_import_path}/spiffegrpc/grpccredentials
    %{go_import_path}/spiffetls*
    %{go_import_path}/svid/jwtsvid
    %{go_import_path}/workloadapi*
}

Name:           go-github-spiffe-go-spiffe-v2
Version:        2.6.0
Release:        %autorelease
Summary:        SPIFFE library for Go
License:        Apache-2.0
URL:            https://github.com/spiffe/go-spiffe
#!RemoteAsset:  sha256:3eb3fc58ee4c038c3074593ad8ae7a44e51141edaa7c981081d134f601bdb169
Source0:        https://github.com/spiffe/go-spiffe/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/spiffe/go-spiffe/v2) = %{version}

Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/check.v1)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides SPIFFE library for Go.

%install -a
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/examples \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/internal/test/fakeworkloadapi \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/proto/spiffe/workload \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/spiffegrpc \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/spiffetls \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/workloadapi

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
