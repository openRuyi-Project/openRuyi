# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name no_std_io2
%global full_version 0.9.4
%global pkgname no-std-io2-0.9

Name:           rust-no-std-io2-0.9
Version:        0.9.4
Release:        %autorelease
Summary:        Rust crate "no_std_io2"
License:        Apache-2.0 OR MIT
URL:            https://github.com/wcampbell0x2a/no-std-io2
#!RemoteAsset:  sha256:418abd1b6d34fbf6cae440dc874771b0525a604428704c76e48b29a5e67b8003
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Alloc support is optional.
Source code for takopackized Rust crate "no_std_io2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
