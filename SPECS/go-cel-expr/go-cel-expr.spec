# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           expr
%define go_import_path  cel.dev/expr

Name:           go-cel-expr
Version:        0.25.1
Release:        %autorelease
Summary:        Common Expression Language -- specification and binary representation
License:        Apache-2.0
URL:            https://github.com/google/cel-spec
#!RemoteAsset
Source0:        https://github.com/google/cel-spec/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(cel.dev/expr) = %{version}

Requires:       go(google.golang.org/protobuf)

%description

The Common Expression Language (CEL) implements common semantics for
expression evaluation, enabling different applications to more easily
interoperate.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
