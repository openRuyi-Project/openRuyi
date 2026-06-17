# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name maybe-rayon
%global full_version 0.1.1
%global pkgname maybe-rayon-0.1

Name:           rust-maybe-rayon-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "maybe-rayon"
License:        MIT
URL:            https://github.com/shssoichiro/maybe-rayon
#!RemoteAsset:  sha256:8ea1f30cedd69f0a2954655f7188c6a834246d2bcf1e315e2ac40c4b24dc9519
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "maybe-rayon"

%package     -n %{name}+rayon
Summary:        Either acts as rayon or creates a single-threaded facade - feature "rayon" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rayon) = %{version}
Provides:       crate(%{pkgname}/threads) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust maybe-rayon crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "threads" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
