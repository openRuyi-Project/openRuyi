# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytecount
%global full_version 0.6.9
%global pkgname bytecount-0.6

Name:           rust-bytecount-0.6
Version:        0.6.9
Release:        %autorelease
Summary:        Rust crate "bytecount"
License:        Apache-2.0 OR MIT
URL:            https://github.com/llogiq/bytecount
#!RemoteAsset:  sha256:175812e0be2bccb6abe50bb8d566126198344f707e304f45c648fd8f2cc0365e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/generic-simd) = %{version}
Provides:       crate(%{pkgname}/html-report) = %{version}
Provides:       crate(%{pkgname}/runtime-dispatch-simd) = %{version}

%description
Source code for takopackized Rust crate "bytecount"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
