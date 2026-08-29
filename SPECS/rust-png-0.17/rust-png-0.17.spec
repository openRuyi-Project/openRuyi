# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name png
%global full_version 0.17.16
%global pkgname png-0.17

Name:           rust-png-0.17
Version:        0.17.16
Release:        %autorelease
Summary:        Rust crate "png"
License:        MIT OR Apache-2.0
URL:            https://github.com/image-rs/image-png
#!RemoteAsset:  sha256:82151a2fc869e011c153adc57cf2789ccb8d9906ce52c0b39a6b5697749d7526
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(crc32fast-1/default) >= 1.2.0
Requires:       crate(fdeflate-0.3/default) >= 0.3.3
Requires:       crate(flate2-1/default) >= 1.0.11
Requires:       crate(miniz-oxide-0.8/default) >= 0.8.0
Requires:       crate(miniz-oxide-0.8/simd) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/benchmarks) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "png"

%package     -n %{name}+unstable
Summary:        PNG decoding and encoding library in pure Rust - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc32fast-1/nightly) >= 1.2.0
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust png crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
