# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parking_lot
%global full_version 0.9.0
%global pkgname parking-lot-0.9

Name:           rust-parking-lot-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "parking_lot"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:f842b1982eb6c2fe34036a4fbfb06dd185a3f5c8edfaacdf7d1ea10b07de6252
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lock-api-0.3/default) >= 0.3.1
Requires:       crate(parking-lot-core-0.6/default) >= 0.6.0
Requires:       crate(rustc-version-0.2) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "parking_lot"

%package     -n %{name}+deadlock-detection
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "deadlock_detection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-core-0.6/deadlock-detection) >= 0.6.0
Provides:       crate(%{pkgname}/deadlock-detection) = %{version}

%description -n %{name}+deadlock-detection
This metapackage enables feature "deadlock_detection" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.3/nightly) >= 0.3.1
Requires:       crate(parking-lot-core-0.6/nightly) >= 0.6.0
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+owning-ref
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "owning_ref"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.3/owning-ref) >= 0.3.1
Provides:       crate(%{pkgname}/owning-ref) = %{version}

%description -n %{name}+owning-ref
This metapackage enables feature "owning_ref" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.3/serde) >= 0.3.1
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
