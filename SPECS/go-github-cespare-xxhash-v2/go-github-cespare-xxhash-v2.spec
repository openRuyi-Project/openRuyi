# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xxhash
%define go_import_path  github.com/cespare/xxhash/v2
%define go_test_include github.com/cespare/xxhash/v2

Name:           go-github-cespare-xxhash-v2
Version:        2.3.0
Release:        %autorelease
Summary:        A Go implementation of the 64-bit xxHash algorithm (XXH64)
License:        MIT
URL:            https://github.com/cespare/xxhash
#!RemoteAsset
Source0:        https://github.com/cespare/xxhash/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cespare/xxhash/v2) = %{version}

%description
xxhash is a Go implementation of the 64-bit xxHash (https://xxhash.com/)
algorithm, XXH64. This is a high-quality hashing algorithm that is much
faster than anything in the Go standard library.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
