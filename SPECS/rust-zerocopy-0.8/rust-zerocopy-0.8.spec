# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy
%global full_version 0.8.50
%global pkgname zerocopy-0.8

Name:           rust-zerocopy-0.8
Version:        0.8.50
Release:        %autorelease
Summary:        Rust crate "zerocopy"
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:3b065d4f0e55f82fae73202e189638116a87c55ab6b8e6c2721e13dd9d854ad1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zerocopy-derive-0.8/default) >= 0.8.50
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/float-nightly) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/simd-nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
We write "unsafe" so you don't have to.
Source code for takopackized Rust crate "zerocopy"

%package     -n %{name}+internal-use-only-features-that-work-on-stable
Summary:        Zerocopy makes zero-cost memory manipulation effortless - feature "__internal_use_only_features_that_work_on_stable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/internal-use-only-features-that-work-on-stable) = %{version}

%description -n %{name}+internal-use-only-features-that-work-on-stable
We write "unsafe" so you don't have to.
This metapackage enables feature "__internal_use_only_features_that_work_on_stable" for the Rust zerocopy crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerocopy-derive
Summary:        Zerocopy makes zero-cost memory manipulation effortless - feature "zerocopy-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerocopy-derive-0.8/default) >= 0.8.50
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/zerocopy-derive) = %{version}

%description -n %{name}+zerocopy-derive
We write "unsafe" so you don't have to.
This metapackage enables feature "zerocopy-derive" for the Rust zerocopy crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
