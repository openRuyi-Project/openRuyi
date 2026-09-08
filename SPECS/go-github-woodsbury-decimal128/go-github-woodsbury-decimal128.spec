# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           decimal128
%define go_import_path  github.com/woodsbury/decimal128

Name:           go-github-woodsbury-decimal128
Version:        1.5.0
Release:        %autorelease
Summary:        Go module implementing support for decimal128 values
License:        BSD-0-Clause
URL:            https://github.com/woodsbury/decimal128
#!RemoteAsset:  sha256:d393be0a8ee4139403dfcbbd28e76e8c4cd542a9172d3e5c629002cf6776814b
Source0:        https://github.com/woodsbury/decimal128/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/woodsbury/decimal128) = %{version}

%description
Package decimal128 provides a 128-bit decimal floating point type.

%files
%license LICENCE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
