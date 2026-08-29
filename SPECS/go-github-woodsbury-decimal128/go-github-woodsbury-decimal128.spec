# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           decimal128
%define go_import_path  github.com/woodsbury/decimal128

Name:           go-github-woodsbury-decimal128
Version:        1.4.0
Release:        %autorelease
Summary:        Go module implementing support for decimal128 values
License:        BSD-0-Clause
URL:            https://github.com/woodsbury/decimal128
#!RemoteAsset:  sha256:f2b39f7e8b7a1907c13edfa9d2700295b6fd74e54214edd94c4d14f909719adc
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
