# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xds
# So the import path technically is github.com/cncf/xds/go
%define go_import_path  github.com/cncf/xds
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id ee656c7534f5d7dc23d44dd611689568f72017a6
# Avoid circular dependency issue with the first two packages
%global go_test_exclude_glob %{shrink:
    google.golang.org/grpc*
    google.golang.org/genproto*
    github.com/cncf/xds/go/xds/service/orca*
    github.com/cncf/xds/go/udpa/service/orca*
    github.com/cncf/xds/go/xds/type*
    github.com/cncf/xds/test/build*
}

Name:           go-github-cncf-xds
Version:        0+git20260107.ee656c7
Release:        %autorelease
Summary:        xDS API Working Group
License:        Apache-2.0
URL:            https://github.com/cncf/xds
#!RemoteAsset
Source0:        https://github.com/cncf/xds/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/cncf/xds/go) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(google.golang.org/protobuf)

%description
The objective of the xDS API Working Group (xDS-WG) is to bring together
parties across the industry interested in a common control and
configuration API for data plane proxies and load balancers, based on
the xDS APIs.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
