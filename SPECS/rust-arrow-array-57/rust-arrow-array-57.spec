# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-array
%global full_version 57.3.1
%global pkgname arrow-array-57

Name:           rust-arrow-array-57
Version:        57.3.1
Release:        %autorelease
Summary:        Rust crate "arrow-array"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:c8a4ab47b3f3eac60f7fd31b81e9028fda018607bcc63451aca4f2b755269862
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/compile-time-rng) >= 0.8.0
Requires:       crate(ahash-0.8/runtime-rng) >= 0.8.0
Requires:       crate(arrow-buffer-57/default) >= 57.3.1
Requires:       crate(arrow-data-57/default) >= 57.3.1
Requires:       crate(arrow-schema-57/default) >= 57.3.1
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(half-2/num-traits) >= 2.1.0
Requires:       crate(hashbrown-0.16) >= 0.16.0
Requires:       crate(num-complex-0.4/std) >= 0.4.6
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/std) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/force-validate) = %{version}

%description
Source code for takopackized Rust crate "arrow-array"

%package     -n %{name}+chrono-tz
Summary:        Array abstractions for Apache Arrow - feature "chrono-tz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-tz-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/chrono-tz) = %{version}

%description -n %{name}+chrono-tz
This metapackage enables feature "chrono-tz" for the Rust arrow-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ffi
Summary:        Array abstractions for Apache Arrow - feature "ffi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-data-57/ffi) >= 57.3.1
Requires:       crate(arrow-schema-57/ffi) >= 57.3.1
Provides:       crate(%{pkgname}/ffi) = %{version}

%description -n %{name}+ffi
This metapackage enables feature "ffi" for the Rust arrow-array crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
