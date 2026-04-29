# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name half
%global full_version 2.7.1
%global pkgname half-2.0

Name:           rust-half-2.0
Version:        2.7.1
Release:        %autorelease
Summary:        Rust crate "half"
License:        MIT OR Apache-2.0
URL:            https://github.com/VoidStarKat/half-rs
#!RemoteAsset:  sha256:6ea2d84b969582b4b1864a92dc5d27cd2b77b622a8d79306834f1be5ba20d84b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(crunchy-0.2/default) >= 0.2.4
Requires:       crate(zerocopy-0.8/derive) >= 0.8.48
Requires:       crate(zerocopy-0.8/simd) >= 0.8.48
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/use-intrinsics)
Provides:       crate(%{pkgname}/zerocopy)

%description
Source code for takopackized Rust crate "half"

%package     -n %{name}+arbitrary
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.4.1
Requires:       crate(arbitrary-1.0/derive) >= 1.4.1
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0/derive) >= 1.4.1
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-traits
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "num-traits"
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/libm) >= 0.2.16
Provides:       crate(%{pkgname}/num-traits)

%description -n %{name}+num-traits
This metapackage enables feature "num-traits" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-distr
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "rand_distr"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.9/thread-rng) >= 0.9.0
Requires:       crate(rand-distr-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/rand-distr)

%description -n %{name}+rand-distr
This metapackage enables feature "rand_distr" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "rkyv"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rkyv)

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
