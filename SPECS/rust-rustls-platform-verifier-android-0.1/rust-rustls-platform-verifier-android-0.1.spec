# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-platform-verifier-android
%global full_version 0.1.1
%global pkgname rustls-platform-verifier-android-0.1

Name:           rust-rustls-platform-verifier-android-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "rustls-platform-verifier-android"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustls/rustls-platform-verifier
#!RemoteAsset:  sha256:f87165f0995f63a9fbeea62b64d10b4d9d8e78ec6d7d51fb2125fda7bb36788f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
You shouldn't depend on this directly.
Source code for takopackized Rust crate "rustls-platform-verifier-android"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
