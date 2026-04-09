# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonparser
%define go_import_path  github.com/buger/jsonparser
%define go_test_exclude_glob github.com/buger/jsonparser/benchmark

Name:           go-github-buger-jsonparser
Version:        1.1.1
Release:        %autorelease
Summary:        One of the fastest alternative JSON parser for Go that does not require schema
License:        MIT
URL:            https://github.com/buger/jsonparser
#!RemoteAsset
Source0:        https://github.com/buger/jsonparser/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/buger/jsonparser) = %{version}

%description
Alternative JSON parser for Go (10x times faster standard library)

It does not require you to know the structure of the payload (eg. create
structs), and allows accessing fields by providing the path to them. It
is up to **10 times faster** than standard encoding/json package
(depending on payload size and usage), **allocates no memory**. See
benchmarks below.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
