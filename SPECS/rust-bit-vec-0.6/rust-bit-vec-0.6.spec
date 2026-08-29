# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bit-vec
%global full_version 0.6.3
%global pkgname bit-vec-0.6

Name:           rust-bit-vec-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "bit-vec"
License:        MIT OR Apache-2.0
URL:            https://github.com/contain-rs/bit-vec
#!RemoteAsset:  sha256:349f9b6a179ed607305526ca489b34ad0a41aed5f7980fa90eb03160b69598fb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bit-vec"

%package     -n %{name}+serde
Summary:        Vector of bits - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-no-std
Summary:        Vector of bits - feature "serde_no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde-no-std) = %{version}

%description -n %{name}+serde-no-std
This metapackage enables feature "serde_no_std" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-std
Summary:        Vector of bits - feature "serde_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-std) = %{version}

%description -n %{name}+serde-std
This metapackage enables feature "serde_std" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
