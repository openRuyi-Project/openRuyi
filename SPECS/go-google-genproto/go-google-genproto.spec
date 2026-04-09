# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# NOTICE:
# DO NOT TRY TO UPGRADE THIS UNLESS YOU ARE VERY FAMILIAR WITH
# THIS IS YOUR FINAL WARNING. - 251

%define _name           genproto
%define go_import_path  google.golang.org/genproto
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id e7812ac95cc0c7174fe2fc2914ed037d4bd20613
# Circular dependency with google.golang.org/grpc - 251
%define go_test_exclude_glob %{shrink:
    google.golang.org/genproto/googleapis*
    google.golang.org/genproto/firestore/bundle
}

Name:           go-google-genproto
Version:        0+git20260107.e7812ac
Release:        %autorelease
Summary:        Generated code for Google Cloud client libraries.
License:        Apache-2.0
URL:            https://github.com/googleapis/go-genproto
#!RemoteAsset
Source0:        https://github.com/googleapis/go-genproto/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)

Provides:       go(google.golang.org/genproto) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(google.golang.org/protobuf)

%description
This repository contains the generated Go packages for common protocol
buffer types, and the generated gRPC (http://grpc.io) code necessary for
interacting with Google's gRPC APIs.

# Circular dependency with google.golang.org/grpc - 251
%package        googleapis-rpc
Summary:        Common Google APIs RPC protos

Provides:       go(google.golang.org/genproto/googleapis/rpc)

%description    googleapis-rpc
This subpackage contains the generated code for common Google APIs RPC
protos.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/googleapis/rpc

%files googleapis-rpc
%{go_sys_gopath}/%{go_import_path}/googleapis/rpc

%changelog
%autochangelog
