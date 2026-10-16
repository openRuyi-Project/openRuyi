# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tiny-keccak
%global full_version 2.0.2
%global pkgname tiny-keccak-2

Name:           rust-tiny-keccak-2
Version:        2.0.2
Release:        %autorelease
Summary:        Rust crate "tiny-keccak"
License:        CC0-1.0
URL:            https://github.com/debris/tiny-keccak
#!RemoteAsset:  sha256:2c9d3793400a45f954c52e73d068316d76b6f4e36977e3fcebb13a2721e80237
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crunchy-0.2/default) >= 0.2.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cshake) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/k12) = %{version}
Provides:       crate(%{pkgname}/keccak) = %{version}
Provides:       crate(%{pkgname}/kmac) = %{version}
Provides:       crate(%{pkgname}/parallel-hash) = %{version}
Provides:       crate(%{pkgname}/sha3) = %{version}
Provides:       crate(%{pkgname}/shake) = %{version}
Provides:       crate(%{pkgname}/tuple-hash) = %{version}

%description
Source code for takopackized Rust crate "tiny-keccak"

%package     -n %{name}+fips202
Summary:        Keccak derived functions - feature "fips202"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/keccak) = %{version}
Requires:       crate(%{pkgname}/sha3) = %{version}
Requires:       crate(%{pkgname}/shake) = %{version}
Provides:       crate(%{pkgname}/fips202) = %{version}

%description -n %{name}+fips202
This metapackage enables feature "fips202" for the Rust tiny-keccak crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sp800
Summary:        Keccak derived functions - feature "sp800"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cshake) = %{version}
Requires:       crate(%{pkgname}/kmac) = %{version}
Requires:       crate(%{pkgname}/tuple-hash) = %{version}
Provides:       crate(%{pkgname}/sp800) = %{version}

%description -n %{name}+sp800
This metapackage enables feature "sp800" for the Rust tiny-keccak crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
