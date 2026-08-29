# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bs58
%global full_version 0.5.1
%global pkgname bs58-0.5

Name:           rust-bs58-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "bs58"
License:        MIT OR Apache-2.0
URL:            https://github.com/Nullus157/bs58-rs
#!RemoteAsset:  sha256:bf88ba1141d185c399bee5288d850d63b8369520c1eafc32a0430b5b6c287bf4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bs58"

%package     -n %{name}+alloc
Summary:        Another Base58 codec implementation - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tinyvec-1/alloc) >= 1.6.0
Requires:       crate(tinyvec-1/grab-spare-slice) >= 1.6.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bs58 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Another Base58 codec implementation - feature "sha2" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/cb58) = %{version}
Provides:       crate(%{pkgname}/check) = %{version}
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust bs58 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cb58", and "check" features.

%package     -n %{name}+smallvec
Summary:        Another Base58 codec implementation - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust bs58 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Another Base58 codec implementation - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(tinyvec-1/grab-spare-slice) >= 1.6.0
Requires:       crate(tinyvec-1/std) >= 1.6.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bs58 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tinyvec
Summary:        Another Base58 codec implementation - feature "tinyvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tinyvec-1/grab-spare-slice) >= 1.6.0
Provides:       crate(%{pkgname}/tinyvec) = %{version}

%description -n %{name}+tinyvec
This metapackage enables feature "tinyvec" for the Rust bs58 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
