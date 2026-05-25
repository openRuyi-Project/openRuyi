# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ratelimit
%define go_import_path  github.com/envoyproxy/go-control-plane

Name:           go-github-envoyproxy-go-control-plane-ratelimit
Version:        0.1.0
Release:        %autorelease
Summary:        Envoy rate limit API module for Go
License:        Apache-2.0
URL:            https://github.com/envoyproxy/go-control-plane
#!RemoteAsset:  sha256:51207d3797250a956531a08d270673f21c479da9163d24b6b70200ab64b54617
Source0:        https://github.com/envoyproxy/go-control-plane/archive/refs/tags/ratelimit/v0.1.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-control-plane-ratelimit-v0.1.0
# The archive is tagged for the ratelimit module, but the generated packages
# live under ratelimit/ while the module path remains github.com/envoyproxy/go-control-plane.
# Keep %check scoped to that subtree so the installed import paths match Provides.
%define go_test_include %{go_import_path}/ratelimit/...

BuildRequires:  go
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy/service/discovery/v3)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/envoyproxy/go-control-plane/ratelimit) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/ratelimit/config/ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/ratelimit/service/ratelimit/v3) = %{version}

Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/envoyproxy/go-control-plane/envoy)
Requires:       go(github.com/envoyproxy/go-control-plane/envoy/service/discovery/v3)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides Envoy rate limit API module for Go.

%install -a
find %{buildroot}%{go_sys_gopath}/%{go_import_path} -mindepth 1 -maxdepth 1 ! -name ratelimit -exec rm -rf {} +

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/ratelimit

%changelog
%autochangelog
