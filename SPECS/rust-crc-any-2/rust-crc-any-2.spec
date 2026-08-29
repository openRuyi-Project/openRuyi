# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crc-any
%global full_version 2.5.0
%global pkgname crc-any-2

Name:           rust-crc-any-2
Version:        2.5.0
Release:        %autorelease
Summary:        Rust crate "crc-any"
License:        MIT
URL:            https://magiclen.org/crc-any
#!RemoteAsset:  sha256:a62ec9ff5f7965e4d7280bd5482acd20aadb50d632cf6c1d74493856b011fa73
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/development) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
It has many built-in CRC functions.
Source code for takopackized Rust crate "crc-any"

%package     -n %{name}+debug-helper
Summary:        To compute CRC values by providing the length of bits, expression, reflection, an initial value and a final xor value - feature "debug-helper" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(debug-helper-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/debug-helper) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+debug-helper
It has many built-in CRC functions.
This metapackage enables feature "debug-helper" for the Rust crc-any crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "alloc", and "default" features.

%package     -n %{name}+heapless
Summary:        To compute CRC values by providing the length of bits, expression, reflection, an initial value and a final xor value - feature "heapless"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heapless-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/heapless) = %{version}

%description -n %{name}+heapless
It has many built-in CRC functions.
This metapackage enables feature "heapless" for the Rust crc-any crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
