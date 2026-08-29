# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rayon-core
%global full_version 1.13.0
%global pkgname rayon-core-1

Name:           rust-rayon-core-1
Version:        1.13.0
Release:        %autorelease
Summary:        Rust crate "rayon-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/rayon-rs/rayon
#!RemoteAsset:  sha256:22e18b0f0062d30d4230b2e85ff77fdfe4326feb054b9783a3460d8435c8ab91
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-deque-0.8/default) >= 0.8.1
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rayon-core"

%package     -n %{name}+web-spin-lock
Summary:        Core APIs for Rayon - feature "web_spin_lock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-sync-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/web-spin-lock) = %{version}

%description -n %{name}+web-spin-lock
This metapackage enables feature "web_spin_lock" for the Rust rayon-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
