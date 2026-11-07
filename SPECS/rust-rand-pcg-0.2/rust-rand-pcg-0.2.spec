# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_pcg
%global full_version 0.2.1
%global pkgname rand-pcg-0.2

Name:           rust-rand-pcg-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "rand_pcg"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_pcg
#!RemoteAsset:  sha256:16abd0c1b639e9eb4d7c50c0b8100b0d0f849be2349829c740fe8e6eb4816429
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_pcg"

%package     -n %{name}+serde
Summary:        Selected PCG random number generators - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_pcg crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde1" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
