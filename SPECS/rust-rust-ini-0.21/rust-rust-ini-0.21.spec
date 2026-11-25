# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust-ini
%global full_version 0.21.3
%global pkgname rust-ini-0.21

Name:           rust-rust-ini-0.21
Version:        0.21.3
Release:        %autorelease
Summary:        Rust crate "rust-ini"
License:        MIT
URL:            https://github.com/zonyitoo/rust-ini
#!RemoteAsset:  sha256:796e8d2b6696392a43bea58116b667fb4c29727dc5abd27d6acf338bb4f688c7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(ordered-multimap-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/brackets-in-section-names) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/inline-comment) = %{version}

%description
Source code for takopackized Rust crate "rust-ini"

%package     -n %{name}+unicase
Summary:        Ini configuration file parsing library in Rust - feature "unicase" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2/default) >= 2.6.0
Provides:       crate(%{pkgname}/case-insensitive) = %{version}
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust rust-ini crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "case-insensitive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
