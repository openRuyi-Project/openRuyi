# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rayon
%global full_version 1.12.0
%global pkgname rayon-1.0

Name:           rust-rayon-1.0
Version:        1.12.0
Release:        %autorelease
Summary:        Rust crate "rayon"
License:        MIT OR Apache-2.0
URL:            https://github.com/rayon-rs/rayon
#!RemoteAsset:  sha256:fb39b166781f92d482534ef4b4b1b2568f42613b53e5b6c160e24cfbfa30926d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1.0) >= 1.15.0
Requires:       crate(rayon-core-1.0/default) >= 1.13.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rayon"

%package     -n %{name}+web-spin-lock
Summary:        Simple work-stealing parallelism for Rust - feature "web_spin_lock"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-core-1.0/web-spin-lock) >= 1.13.0
Requires:       crate(wasm-sync-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/web-spin-lock)

%description -n %{name}+web-spin-lock
This metapackage enables feature "web_spin_lock" for the Rust rayon crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
