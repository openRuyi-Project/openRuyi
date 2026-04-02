# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-common
%global full_version 0.1.6
%global pkgname crypto-common-0.1

Name:           rust-crypto-common-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "crypto-common"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:1bfb12502f3fc46cca1bb51ac28df9d618d813cdc3d2f25b9fe775a34af26bb3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(generic-array-0.14/default) >= 0.14.9
Requires:       crate(generic-array-0.14/more-lengths) >= 0.14.9
Requires:       crate(typenum-1.0/default) >= 1.19.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "crypto-common"

%package     -n %{name}+getrandom
Summary:        Common cryptographic traits - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.0
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Common cryptographic traits - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
