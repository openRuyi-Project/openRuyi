# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# NOTICE:
# DO NOT TRY TO UPGRADE THIS UNLESS YOU ARE VERY FAMILIAR WITH
# THIS IS YOUR FINAL WARNING. - 251

%define _name           genproto
%define go_import_path  google.golang.org/genproto
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id e7812ac95cc0c7174fe2fc2914ed037d4bd20613
%define api_commit f6391c0de4c7faa7ff952a3e47cf1dd2cdb18aaf
# Circular dependency with google.golang.org/grpc - 251
%define go_test_exclude_glob %{shrink:
    google.golang.org/genproto/googleapis*
    google.golang.org/genproto/firestore/bundle
}

Name:           go-google-genproto
Version:        0+git20260107.e7812ac
Release:        %autorelease
Summary:        Generated code for Google Cloud client libraries
License:        Apache-2.0
URL:            https://github.com/googleapis/go-genproto
#!RemoteAsset:  sha256:ee9bdfda880edd9348440dd2ec43a1cf9cf4e0b70b06f0cdd1ec7aa8515f1358
Source0:        https://github.com/googleapis/go-genproto/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:5d7f61221fea378b9699169d4a4fe43b55358071bdedc7b297c713697b85ee59
Source1:        https://github.com/googleapis/go-genproto/archive/%{api_commit}.tar.gz#/%{_name}-googleapis-api-%{api_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(google.golang.org/genproto) = %{version}
Provides:       go(google.golang.org/genproto/googleapis/api) = %{version}

Requires:       %{name}-googleapis-rpc = %{version}-%{release}
Requires:       go(github.com/golang/protobuf)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This repository contains the generated Go packages for common protocol
buffer types, and the generated gRPC (http://grpc.io) code necessary for
interacting with Google's gRPC APIs.

# Circular dependency with google.golang.org/grpc - 251
%package        googleapis-rpc
Summary:        Common Google APIs RPC protos

Provides:       go(google.golang.org/genproto/googleapis/rpc) = %{version}

%description    googleapis-rpc
This subpackage contains the generated code for common Google APIs RPC
protos.

%prep -a
tar -xzf %{SOURCE1}
rm -rf googleapis/api
cp -a "go-%{_name}-%{api_commit}/googleapis/api" googleapis/
rm -rf "go-%{_name}-%{api_commit}"

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/googleapis/rpc

%files googleapis-rpc
%{go_sys_gopath}/%{go_import_path}/googleapis/rpc

%changelog
%autochangelog
