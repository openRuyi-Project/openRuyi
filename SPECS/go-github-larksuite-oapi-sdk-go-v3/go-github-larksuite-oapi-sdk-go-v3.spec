# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           oapi-sdk-go
%define go_import_path  github.com/larksuite/oapi-sdk-go/v3
%define go_test_exclude %{shrink:
    %{go_import_path}/core
    %{go_import_path}/channel/safety
}
%define go_test_exclude_glob %{go_import_path}/sample/*

Name:           go-github-larksuite-oapi-sdk-go-v3
Version:        3.9.4
Release:        %autorelease
Summary:        Feishu OpenPlatform Server SDK
License:        MIT
URL:            https://github.com/larksuite/oapi-sdk-go
#!RemoteAsset:  sha256:2496af6150583facd6161bb87d4bdab62f159225cbf8ded9a97f2598c91f8aa3
Source0:        https://github.com/larksuite/oapi-sdk-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/gorilla/websocket)

Provides:       go(github.com/larksuite/oapi-sdk-go/v3) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/gorilla/websocket)

%description
Feishu Open Platform offers a series of server-side atomic APIs to achieve
diverse functionalities. However, actual coding requires additional work, such
as obtaining and maintaining access tokens, encrypting and decrypting data,
and verifying request signatures. Furthermore, the lack of semantic
descriptions for function calls and type system support can increase coding
burdens.

To address these issues, Feishu Open Platform has developed the Open Interface
SDK, which incorporates all lengthy logic processes, provides a comprehensive
type system, and offers a semantic programming interface to enhance the coding
experience.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
