# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parking_lot
%global full_version 0.12.5
%global pkgname parking-lot-0.12

Name:           rust-parking-lot-0.12
Version:        0.12.5
Release:        %autorelease
Summary:        Rust crate "parking_lot"
License:        MIT OR Apache-2.0
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:93857453250e3077bd71ff98b6a65ea6621a19bb0f559a85248955ac12c45a1a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lock-api-0.4/default) >= 0.4.14
Requires:       crate(parking-lot-core-0.9/default) >= 0.9.12
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/hardware-lock-elision)
Provides:       crate(%{pkgname}/send-guard)

%description
Source code for takopackized Rust crate "parking_lot"

%package     -n %{name}+arc-lock
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "arc_lock"
Requires:       crate(%{pkgname})
Requires:       crate(lock-api-0.4/arc-lock) >= 0.4.14
Provides:       crate(%{pkgname}/arc-lock)

%description -n %{name}+arc-lock
This metapackage enables feature "arc_lock" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deadlock-detection
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "deadlock_detection"
Requires:       crate(%{pkgname})
Requires:       crate(parking-lot-core-0.9/deadlock-detection) >= 0.9.12
Provides:       crate(%{pkgname}/deadlock-detection)

%description -n %{name}+deadlock-detection
This metapackage enables feature "deadlock_detection" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "nightly"
Requires:       crate(%{pkgname})
Requires:       crate(lock-api-0.4/nightly) >= 0.4.14
Requires:       crate(parking-lot-core-0.9/nightly) >= 0.9.12
Provides:       crate(%{pkgname}/nightly)

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+owning-ref
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "owning_ref"
Requires:       crate(%{pkgname})
Requires:       crate(lock-api-0.4/owning-ref) >= 0.4.14
Provides:       crate(%{pkgname}/owning-ref)

%description -n %{name}+owning-ref
This metapackage enables feature "owning_ref" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(lock-api-0.4/serde) >= 0.4.14
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
