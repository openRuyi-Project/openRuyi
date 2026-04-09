# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xxhash
%define go_import_path  github.com/cespare/xxhash

Name:           go-github-cespare-xxhash
Version:        1.1.0
Release:        %autorelease
Summary:        A Go implementation of the 64-bit xxHash algorithm (XXH64)
License:        MIT
URL:            https://github.com/cespare/xxhash
#!RemoteAsset
Source0:        https://github.com/cespare/xxhash/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/OneOfOne/xxhash)
BuildRequires:  go(github.com/spaolacci/murmur3)

Provides:       go(github.com/cespare/xxhash) = %{version}

Requires:       go(github.com/OneOfOne/xxhash)
Requires:       go(github.com/spaolacci/murmur3)

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
