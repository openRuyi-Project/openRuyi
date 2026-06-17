# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name adler2
%global full_version 2.0.1
%global pkgname adler2-2

Name:           rust-adler2-2
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "adler2"
License:        0BSD OR MIT OR Apache-2.0
URL:            https://github.com/oyvindln/adler2
#!RemoteAsset:  sha256:320119579fcad9c21884f5c4861d16174d0e06250625266f50fe6898340abefa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "adler2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
