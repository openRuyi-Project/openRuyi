# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golang_protobuf_extensions
%define go_import_path  github.com/matttproud/golang_protobuf_extensions

Name:           go-github-matttproud-golang-protobuf-extensions
Version:        1.0.4
Release:        %autorelease
Summary:        Protocol Buffer streaming helpers for Go
License:        Apache-2.0
URL:            https://github.com/matttproud/golang_protobuf_extensions
#!RemoteAsset:  sha256:b64cab9cb9ae8b9162c7197aeedc6ed617b4c93e4f5674c3ec6cd2e9b0d9d09c
Source0:        https://github.com/matttproud/golang_protobuf_extensions/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)

Provides:       go(github.com/matttproud/golang_protobuf_extensions) = %{version}

Requires:       go(github.com/golang/protobuf)

%description
This package provides Go helpers for working with length-delimited
Protocol Buffer message streams.

%files
%doc README.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
