# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cbor
%define go_import_path  github.com/fxamacker/cbor/v2

Name:           go-github-fxamacker-cbor-v2
Version:        2.9.4
Release:        %autorelease
Summary:        CBOR codec for Go
License:        MIT
URL:            https://github.com/fxamacker/cbor
#!RemoteAsset:  sha256:a9061036e2d017eabcdbce2308ee61aa91d4e242154cc9896d114dbbb3bc72f0
Source0:        https://github.com/fxamacker/cbor/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects the Decode test because the Errorf arguments are
# swapped relative to the format string. - HNO3Miracle
Patch2000:      2000-fix-decode-test-errorf-argument-order.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/x448/float16)

Provides:       go(github.com/fxamacker/cbor/v2) = %{version}

Requires:       go(github.com/x448/float16)

%description
This package provides a CBOR encoder and decoder for Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
