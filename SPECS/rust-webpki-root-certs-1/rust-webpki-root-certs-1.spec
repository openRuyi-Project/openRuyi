# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name webpki-root-certs
%global full_version 1.0.7
%global pkgname webpki-root-certs-1

Name:           rust-webpki-root-certs-1
Version:        1.0.7
Release:        %autorelease
Summary:        Rust crate "webpki-root-certs"
License:        CDLA-Permissive-2.0
URL:            https://github.com/rustls/webpki-roots
#!RemoteAsset:  sha256:f31141ce3fc3e300ae89b78c0dd67f9708061d1d2eda54b8209346fd6be9a92c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-pki-types-1) >= 1.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "webpki-root-certs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
