# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xxhash
%define go_import_path  github.com/OneOfOne/xxhash
# Avoid circular dependency with github.com/cespare/xxhash - 251
%define go_test_exclude github.com/OneOfOne/xxhash/benchmarks

Name:           go-github-oneofone-xxhash
Version:        1.2.8
Release:        %autorelease
Summary:        A native implementation of the excellent XXHash hashing algorithm.
License:        Apache-2.0
URL:            https://github.com/OneOfOne/xxhash
#!RemoteAsset
Source0:        https://github.com/OneOfOne/xxhash/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/OneOfOne/xxhash) = %{version}

%description
This is a native Go implementation of the excellent xxhash
(https://github.com/Cyan4973/xxHash)* algorithm, an extremely fast non-
cryptographic Hash algorithm, working at speeds close to RAM limits.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
