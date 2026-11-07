# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_chacha
%global full_version 0.2.2
%global pkgname rand-chacha-0.2

Name:           rust-rand-chacha-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "rand_chacha"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_chacha
#!RemoteAsset:  sha256:f4c8ed856279c9737206bf725bf36935d8666ead7aa69b52be55af369d193402
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ppv-lite86-0.2/simd) >= 0.2.6
Requires:       crate(rand-core-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}

%description
Source code for takopackized Rust crate "rand_chacha"

%package     -n %{name}+default
Summary:        ChaCha random number generator - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rand_chacha crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        ChaCha random number generator - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ppv-lite86-0.2/simd) >= 0.2.6
Requires:       crate(ppv-lite86-0.2/std) >= 0.2.6
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand_chacha crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
