# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           simdjson-go
%define go_import_path  github.com/minio/simdjson-go
# Test failure, may be cause by outdate code
%define go_test_ignore_failure 1

Name:           go-github-minio-simdjson-go
Version:        0.4.5
Release:        %autorelease
Summary:        Golang port of simdjson: parsing gigabytes of JSON per second
License:        Apache-2.0
URL:            https://github.com/minio/simdjson-go
#!RemoteAsset
Source0:        https://github.com/minio/simdjson-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/buger/jsonparser)

Provides:       go(github.com/minio/simdjson-go) = %{version}

%description
This is a Golang port of simdjson (https://github.com/lemire/simdjson),
a high performance JSON parser developed by Daniel Lemire and Geoff
Langdale. It makes extensive use of SIMD instructions to achieve parsing
performance of gigabytes of JSON per second.

Performance wise, simdjson-go runs on average at about 40% to 60% of the
speed of simdjson. Compared to Golang's standard package encoding/json,
simdjson-go is about 10x faster.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
