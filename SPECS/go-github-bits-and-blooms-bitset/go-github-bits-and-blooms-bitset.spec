# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bitset
%define go_import_path  github.com/bits-and-blooms/bitset

Name:           go-github-bits-and-blooms-bitset
Version:        1.24.5
Release:        %autorelease
Summary:        Bitset implementation for Go
License:        BSD-3-Clause
URL:            https://github.com/bits-and-blooms/bitset
#!RemoteAsset:  sha256:85dee826b8b80479edbabc156efbfd15e9a22b49ae90e3741392f461a552ae63
Source0:        https://github.com/bits-and-blooms/bitset/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bits-and-blooms/bitset) = %{version}

%description
This package provides Bitset implementation for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
