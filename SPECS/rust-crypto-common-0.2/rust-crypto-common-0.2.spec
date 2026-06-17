# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-common
%global full_version 0.2.2
%global pkgname crypto-common-0.2

Name:           rust-crypto-common-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "crypto-common"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:ce6e4c961d6cd6c9a86db418387425e8bdeaf05b3c8bc1411e6dca4c252f1453
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hybrid-array-0.4/default) >= 0.4.7
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "crypto-common"

%package     -n %{name}+getrandom
Summary:        Common traits used by cryptographic algorithms - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(getrandom-0.4/sys-rng) >= 0.4.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Common traits used by cryptographic algorithms - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Common traits used by cryptographic algorithms - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.7
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
