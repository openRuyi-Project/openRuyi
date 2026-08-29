# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           martian
%define go_import_path  github.com/google/martian/v3
%define commit_id 0f7e6797a04da412118541344bbe0d65945e24c9
# The h2 tests require google.golang.org/genproto/googleapis/rpc/status, which
# is not currently packaged separately; other excluded packages fail under the
# current Go toolchain because of vet/static content-type assertions. - HNO3Miracle
%define go_test_exclude %{shrink:
    %{go_import_path}/cmd/proxy
    %{go_import_path}/h2
    %{go_import_path}/h2/testing
    %{go_import_path}/h2/testservice
    %{go_import_path}/static
    %{go_import_path}/trafficshape
}

Name:           go-github-google-martian-v3
Version:        0+git20260607.0f7e679
Release:        %autorelease
Summary:        Programmable HTTP proxy library for Go
License:        Apache-2.0
URL:            https://github.com/google/martian
#!RemoteAsset:  sha256:69f70554675b4946fd32131c17c565ad9825b427717def7995fb2687233e79a3
Source0:        https://github.com/google/martian/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet reports Fatalf %q with an int argument in har tests; keep tests
# enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/google/martian/v3) = %{version}

Requires:       go(github.com/golang/snappy)
Requires:       go(golang.org/x/net)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides a programmable HTTP proxy library for Go.

%files
%doc CONTRIBUTING
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
