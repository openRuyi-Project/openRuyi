# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protobuf
%define go_import_path  github.com/gogo/protobuf
# So tired, can't stand more flaky tests - 251
%define go_test_exclude_glob %{shrink:
    github.com/gogo/protobuf/protoc-gen-gogo
    github.com/gogo/protobuf/test/dashfilename
    github.com/gogo/protobuf/test/embedconflict
    github.com/gogo/protobuf/test/issue270
}

Name:           go-github-gogo-protobuf
Version:        1.3.2
Release:        %autorelease
Summary:        Protocol Buffers for Go with Gadgets
License:        BSD-3-Clause
URL:            https://github.com/gogo/protobuf
#!RemoteAsset
Source0:        https://github.com/gogo/protobuf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gogo/protobuf) = %{version}

%description
gogoprotobuf is a fork of golang/protobuf with extra code generation
features.

This code generation is used to achieve:

 * fast marshalling and unmarshalling
 * more canonical Go structures
 * goprotobuf compatibility
 * less typing by optionally generating extra helper code
 * peace of mind by optionally generating test and benchmark code
 * other serialization formats

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
