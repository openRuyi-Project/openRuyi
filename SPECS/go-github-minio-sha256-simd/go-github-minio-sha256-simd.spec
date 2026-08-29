# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sha256-simd
%define go_import_path  github.com/minio/sha256-simd

Name:           go-github-minio-sha256-simd
Version:        1.0.0
Release:        %autorelease
Summary:        Accelerated SHA-256 implementation for Go
License:        Apache-2.0
URL:            https://github.com/minio/sha256-simd
#!RemoteAsset:  sha256:f992f67a47d16983f9bab99203aaab044618f13ca1de507c33a70a53de8331e0
Source0:        https://github.com/minio/sha256-simd/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/cpuid/v2)

Provides:       go(github.com/minio/sha256-simd) = %{version}

Requires:       go(github.com/klauspost/cpuid/v2)

%description
sha256-simd provides accelerated SHA-256 implementations for supported CPUs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
