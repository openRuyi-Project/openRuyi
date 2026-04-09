# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           arrow-go
%define go_import_path  github.com/apache/arrow/go/v18
# TODO: this package needs a lot of unpackaged build dependencies... - 251
%global go_test_ignore_failure 1

Name:           go-github-apache-arrow-go-v18
Version:        18.5.0
Release:        %autorelease
Summary:        Official Go implementation of Apache Arrow
License:        Apache-2.0
URL:            https://github.com/apache/arrow-go
#!RemoteAsset
Source0:        https://github.com/apache/arrow-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/flatbuffers)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/xerrors)

Provides:       go(github.com/apache/arrow/go/v18) = %{version}

%description
Apache Arrow (https://arrow.apache.org) is a cross-language development
platform for in-memory data. It specifies a standardized language-
independent columnar memory format for flat and hierarchical data,
organized for efficient analytic operations on modern hardware. It also
provides computational libraries and zero-copy streaming messaging and
inter-process communication.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
