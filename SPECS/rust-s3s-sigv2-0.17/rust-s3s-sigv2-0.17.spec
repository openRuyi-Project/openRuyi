# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name s3s-sigv2
%global full_version 0.17.0
%global pkgname s3s-sigv2-0.17

Name:           rust-s3s-sigv2-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "s3s-sigv2"
License:        Apache-2.0
URL:            https://github.com/Nugine/s3s
#!RemoteAsset:  sha256:0979baf8cdf30e38bdfba8e58ee2776d78e55bb3bd3d1f3502f917829da79933
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-simd-0.8/default) >= 0.8.0
Requires:       crate(hmac-0.13/default) >= 0.13.0
Requires:       crate(jiff-0.2/default) >= 0.2.35
Requires:       crate(sha1-0.11/default) >= 0.11.0
Requires:       crate(smallvec-1/default) >= 1.15.2
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "s3s-sigv2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
