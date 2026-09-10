# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mmh3
%define go_import_path  github.com/DataDog/mmh3
%define commit_id       012dc69a9e49ffc8ea75406d83c36b507caeea6b

Name:           go-github-datadog-mmh3
Version:        0+git20260817.012dc69
Release:        %autorelease
Summary:        MurmurHash3 functions implemented in pure Go
License:        MIT
URL:            https://github.com/DataDog/mmh3
#!RemoteAsset:  sha256:114dd4cb316ef1507e8a3cf33a84a9ef8742a08ae94a234688319b70be1aad18
Source0:        https://github.com/DataDog/mmh3/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

%description
Mmh3 implements the 32-bit and 128-bit variants of MurmurHash3 in pure Go,
including an optimized little-endian 128-bit function.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
