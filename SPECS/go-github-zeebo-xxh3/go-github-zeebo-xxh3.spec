# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xxh3
%define go_import_path  github.com/zeebo/xxh3

Name:           go-github-zeebo-xxh3
Version:        1.0.2
Release:        %autorelease
Summary:        XXH3 algorithm in Go
License:        BSD-2-Clause
URL:            https://github.com/zeebo/xxh3
#!RemoteAsset
Source0:        https://github.com/zeebo/xxh3/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/zeebo/assert)
BuildRequires:  go(github.com/mmcloughlin/avo)
BuildRequires:  go(github.com/cespare/xxhash)

Provides:       go(github.com/zeebo/xxh3) = %{version}

Requires:       go(github.com/klauspost/cpuid/v2)
Requires:       go(github.com/zeebo/assert)
Requires:       go(github.com/mmcloughlin/avo)
Requires:       go(github.com/cespare/xxhash)

%description
This package is a port of the xxh3 (https://github.com/Cyan4973/xxHash)
library to Go.

Upstream has fixed the output as of v0.8.0, and this package matches
that.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
