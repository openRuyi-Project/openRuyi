# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-common
%global full_version 0.2.1
%global pkgname crypto-common-0.2

Name:           rust-crypto-common-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "crypto-common"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:77727bb15fa921304124b128af125e7e3b968275d1b108b379190264f4423710
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hybrid-array-0.4/default) >= 0.4.11
Provides:       crate(crypto-common) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "crypto-common"

%package     -n %{name}+getrandom
Summary:        Common traits used by cryptographic algorithms - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rand-core)
Requires:       crate(getrandom-0.4/default) >= 0.4.2
Requires:       crate(getrandom-0.4/sys-rng) >= 0.4.2
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Common traits used by cryptographic algorithms - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.10/default) >= 0.10.1
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Common traits used by cryptographic algorithms - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.11
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
