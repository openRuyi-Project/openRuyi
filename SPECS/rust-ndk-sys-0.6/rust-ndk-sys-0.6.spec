# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ndk-sys
%global full_version 0.6.0+11769913
%global pkgname ndk-sys-0.6

Name:           rust-ndk-sys-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "ndk-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-mobile/ndk
#!RemoteAsset:  sha256:ee6cda3051665f1fb8d9e08fc35c96d5a244fb1be711a03b71118828afc9a873
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(jni-sys-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/audio) = %{version}
Provides:       crate(%{pkgname}/bitmap) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/media) = %{version}
Provides:       crate(%{pkgname}/nativewindow) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description
Source code for takopackized Rust crate "ndk-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
