# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand
%global full_version 0.10.1
%global pkgname rand-0.10

Name:           rust-rand-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "rand"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:d2e8e8bcc7961af1fdac401278c6a831614941f6164ee3bf4ce61b7edb162207
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/simd-support) = %{version}
Provides:       crate(%{pkgname}/unbiased) = %{version}

%description
Source code for takopackized Rust crate "rand"

%package     -n %{name}+chacha
Summary:        Random number generators and other randomness functionality - feature "chacha" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chacha20-0.10/rng) >= 0.10.0
Provides:       crate(%{pkgname}/chacha) = %{version}
Provides:       crate(%{pkgname}/std-rng) = %{version}

%description -n %{name}+chacha
This metapackage enables feature "chacha" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std_rng" feature.

%package     -n %{name}+default
Summary:        Random number generators and other randomness functionality - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/std-rng) = %{version}
Requires:       crate(%{pkgname}/sys-rng) = %{version}
Requires:       crate(%{pkgname}/thread-rng) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Random number generators and other randomness functionality - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.103
Requires:       crate(serde-1/derive) >= 1.0.103
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Random number generators and other randomness functionality - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(getrandom-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sys-rng
Summary:        Random number generators and other randomness functionality - feature "sys_rng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(getrandom-0.4/sys-rng) >= 0.4.0
Provides:       crate(%{pkgname}/sys-rng) = %{version}

%description -n %{name}+sys-rng
This metapackage enables feature "sys_rng" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thread-rng
Summary:        Random number generators and other randomness functionality - feature "thread_rng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/std-rng) = %{version}
Requires:       crate(%{pkgname}/sys-rng) = %{version}
Provides:       crate(%{pkgname}/thread-rng) = %{version}

%description -n %{name}+thread-rng
This metapackage enables feature "thread_rng" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
