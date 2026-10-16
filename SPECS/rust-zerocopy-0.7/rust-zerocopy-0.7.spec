# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy
%global full_version 0.7.35
%global pkgname zerocopy-0.7

Name:           rust-zerocopy-0.7
Version:        0.7.35
Release:        %autorelease
Summary:        Rust crate "zerocopy"
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:1b9b4fd18abc82b8136838da5d50bae7bdea537c574d8dc1a34ed098d6c166f0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zerocopy-derive-0.7/default) >= 0.7.35

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/simd-nightly) = %{version}

%description
Source code for takopackized Rust crate "zerocopy"

%package     -n %{name}+internal-use-only-features-that-work-on-stable
Summary:        Utilities for zero-copy parsing and serialization - feature "__internal_use_only_features_that_work_on_stable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/internal-use-only-features-that-work-on-stable) = %{version}

%description -n %{name}+internal-use-only-features-that-work-on-stable
This metapackage enables feature "__internal_use_only_features_that_work_on_stable" for the Rust zerocopy crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+byteorder
Summary:        Utilities for zero-copy parsing and serialization - feature "byteorder" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(byteorder-1) >= 1.3.0
Provides:       crate(%{pkgname}/byteorder) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+byteorder
This metapackage enables feature "byteorder" for the Rust zerocopy crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+zerocopy-derive
Summary:        Utilities for zero-copy parsing and serialization - feature "zerocopy-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerocopy-derive-0.7/default) >= 0.7.35
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/zerocopy-derive) = %{version}

%description -n %{name}+zerocopy-derive
This metapackage enables feature "zerocopy-derive" for the Rust zerocopy crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
