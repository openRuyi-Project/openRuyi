# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_chacha
%global full_version 0.9.0
%global pkgname rand-chacha-0.9

Name:           rust-rand-chacha-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "rand_chacha"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:d3022b5f1df60f26e1ffddd6c66e8aa15de382ae63b3a0c1bfc0e4d3e3f325cb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ppv-lite86-0.2/simd) >= 0.2.21
Requires:       crate(rand-core-0.9/default) >= 0.9.5
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "rand_chacha"

%package     -n %{name}+os-rng
Summary:        ChaCha random number generator - feature "os_rng"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.9/os-rng) >= 0.9.5
Provides:       crate(%{pkgname}/os-rng)

%description -n %{name}+os-rng
This metapackage enables feature "os_rng" for the Rust rand_chacha crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        ChaCha random number generator - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_chacha crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        ChaCha random number generator - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(ppv-lite86-0.2/simd) >= 0.2.21
Requires:       crate(ppv-lite86-0.2/std) >= 0.2.21
Requires:       crate(rand-core-0.9/std) >= 0.9.5
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand_chacha crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
