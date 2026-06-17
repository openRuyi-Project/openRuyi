# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name honggfuzz
%global full_version 0.5.60
%global pkgname honggfuzz-0.5

Name:           rust-honggfuzz-0.5
Version:        0.5.60
Release:        %autorelease
Summary:        Rust crate "honggfuzz"
License:        MIT OR Apache-2.0 OR Unlicense OR WTFPL
URL:            https://github.com/rust-fuzz/honggfuzz-rs/blob/master/README.md
#!RemoteAsset:  sha256:4d6510a410acedd7a7683b3a45dafdc5ccf3c72d6addaa373497005964fc4e23
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Requires:       crate(rustc-version-0.4/default) >= 0.4.0
Requires:       crate(semver-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "honggfuzz"

%package     -n %{name}+arbitrary
Summary:        Fuzz your Rust code with Google-developped Honggfuzz ! - feature "arbitrary" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust honggfuzz crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
