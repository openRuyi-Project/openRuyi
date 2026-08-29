# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ppv-lite86
%global full_version 0.2.21
%global pkgname ppv-lite86-0.2

Name:           rust-ppv-lite86-0.2
Version:        0.2.21
Release:        %autorelease
Summary:        Rust crate "ppv-lite86"
License:        MIT OR Apache-2.0
URL:            https://github.com/cryptocorrosion/cryptocorrosion
#!RemoteAsset:  sha256:85eae3c4ed2f50dcfe72643da4befc30deadb458a9b590d720cde2f2b1e97da9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zerocopy-0.8/default) >= 0.8.23
Requires:       crate(zerocopy-0.8/simd) >= 0.8.23
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-simd) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ppv-lite86"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
