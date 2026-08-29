# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cobs
%global full_version 0.3.0
%global pkgname cobs-0.3

Name:           rust-cobs-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "cobs"
License:        MIT OR Apache-2.0
URL:            https://github.com/jamesmunns/cobs.rs
#!RemoteAsset:  sha256:0fa961b519f0b462e3a3b4a34b64d119eeaca1d59af726fe450bbba07a9fc0a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-2) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
COBS is an algorithm for transforming a message into an encoding where a specific value     (the "sentinel" value) is not used. This value can then be used to mark frame boundaries     in a serial communication channel.
Source code for takopackized Rust crate "cobs"

%package     -n %{name}+defmt
Summary:        The Consistent Overhead Byte Stuffing (COBS) algorithm - feature "defmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/defmt) = %{version}

%description -n %{name}+defmt
COBS is an algorithm for transforming a message into an encoding where a specific value     (the "sentinel" value) is not used. This value can then be used to mark frame boundaries     in a serial communication channel.
This metapackage enables feature "defmt" for the Rust cobs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The Consistent Overhead Byte Stuffing (COBS) algorithm - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
COBS is an algorithm for transforming a message into an encoding where a specific value     (the "sentinel" value) is not used. This value can then be used to mark frame boundaries     in a serial communication channel.
This metapackage enables feature "serde" for the Rust cobs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        The Consistent Overhead Byte Stuffing (COBS) algorithm - feature "std" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(thiserror-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description -n %{name}+std
COBS is an algorithm for transforming a message into an encoding where a specific value     (the "sentinel" value) is not used. This value can then be used to mark frame boundaries     in a serial communication channel.
This metapackage enables feature "std" for the Rust cobs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "use_std" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
