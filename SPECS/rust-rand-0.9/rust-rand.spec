# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand
%global full_version 0.9.4
%global pkgname rand-0.9

Name:           rust-rand-0.9
Version:        0.9.4
Release:        %autorelease
Summary:        Rust crate "rand"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:44c5af06bb1b7d3216d91932aed5265164bf384dc89cd6ba05cf59a35f5f76ea
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.9) >= 0.9.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/simd-support)
Provides:       crate(%{pkgname}/small-rng)
Provides:       crate(%{pkgname}/unbiased)

%description
Source code for takopackized Rust crate "rand"

%package     -n %{name}+default
Summary:        Random number generators and other randomness functionality - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/os-rng)
Requires:       crate(%{pkgname}/small-rng)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/std-rng)
Requires:       crate(%{pkgname}/thread-rng)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+os-rng
Summary:        Random number generators and other randomness functionality - feature "os_rng"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.9/os-rng) >= 0.9.5
Provides:       crate(%{pkgname}/os-rng)

%description -n %{name}+os-rng
This metapackage enables feature "os_rng" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Random number generators and other randomness functionality - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.9/serde) >= 0.9.5
Requires:       crate(serde-1.0/default) >= 1.0.103
Requires:       crate(serde-1.0/derive) >= 1.0.103
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Random number generators and other randomness functionality - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(rand-chacha-0.9/std) >= 0.9.0
Requires:       crate(rand-core-0.9/std) >= 0.9.5
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std-rng
Summary:        Random number generators and other randomness functionality - feature "std_rng"
Requires:       crate(%{pkgname})
Requires:       crate(rand-chacha-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/std-rng)

%description -n %{name}+std-rng
This metapackage enables feature "std_rng" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thread-rng
Summary:        Random number generators and other randomness functionality - feature "thread_rng"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/os-rng)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/std-rng)
Provides:       crate(%{pkgname}/thread-rng)

%description -n %{name}+thread-rng
This metapackage enables feature "thread_rng" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
