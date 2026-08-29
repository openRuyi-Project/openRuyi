# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jni-sys-macros
%global full_version 0.4.1
%global pkgname jni-sys-macros-0.4

Name:           rust-jni-sys-macros-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "jni-sys-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/jni-rs/jni-sys
#!RemoteAsset:  sha256:38c0b942f458fe50cdac086d2f946512305e5631e720728f2a61aabcd47a6264
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "jni-sys-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
