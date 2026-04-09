# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protoc-gen-validate
%define go_import_path  github.com/envoyproxy/protoc-gen-validate
# Ghost - 251
%define go_test_exclude_glob github.com/envoyproxy/protoc-gen-validate/tests/harness*

Name:           go-github-envoyproxy-protoc-gen-validate
Version:        1.3.0
Release:        %autorelease
Summary:        Protocol Buffer Validation
License:        Apache-2.0
URL:            https://github.com/envoyproxy/protoc-gen-validate
#!RemoteAsset
Source0:        https://github.com/envoyproxy/protoc-gen-validate/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/iancoleman/strcase)
BuildRequires:  go(github.com/lyft/protoc-gen-star/v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/envoyproxy/protoc-gen-validate) = %{version}

Requires:       go(github.com/iancoleman/strcase)
Requires:       go(github.com/lyft/protoc-gen-star/v2)
Requires:       go(golang.org/x/net)
Requires:       go(google.golang.org/protobuf)

%description
PGV is a protoc plugin to generate polyglot message validators. While
protocol buffers effectively guarantee the types of structured data,
they cannot enforce semantic rules for values. This plugin adds support
to protoc-generated code to validate such constraints.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
