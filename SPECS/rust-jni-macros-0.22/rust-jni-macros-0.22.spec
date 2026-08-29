# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jni-macros
%global full_version 0.22.4
%global pkgname jni-macros-0.22

Name:           rust-jni-macros-0.22
Version:        0.22.4
Release:        %autorelease
Summary:        Rust crate "jni-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/jni-rs/jni-rs
#!RemoteAsset:  sha256:a00109accc170f0bdb141fed3e393c565b6f5e072365c3bd58f5b062591560a3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(rustc-version-0.4) >= 0.4.0
Requires:       crate(simd-cesu8-1/default) >= 1.0.1
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "jni-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
