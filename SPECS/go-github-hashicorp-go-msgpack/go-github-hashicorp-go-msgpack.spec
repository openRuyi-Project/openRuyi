# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-msgpack
%define go_import_path  github.com/hashicorp/go-msgpack

Name:           go-github-hashicorp-go-msgpack
Version:        2.1.5
Release:        %autorelease
Summary:        Open-Source Go Code. msgpack.org[Go]
License:        MIT
URL:            https://github.com/hashicorp/go-msgpack
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-msgpack/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/tools)

%description
This repository contains the go-msgpack library.

Package codec provides a High Performance, Feature-Rich Idiomatic
codec/encoding library for msgpack, json.

Supported Serialization formats are:

 * msgpack: (https://github.com/msgpack/msgpack)
 * json:    (http://json.org) (http://tools.ietf.org/html/rfc7159)

For detailed usage information, read the primer at
(http://ugorji.net/blog/go-codec-primer) .

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
