# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name shake
%global full_version 0.1.0
%global pkgname shake-0.1

Name:           rust-shake-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "shake"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/XOFs
#!RemoteAsset:  sha256:09057cb2149ad4cbd2da1e26b351f9a4c354219421229c69c3063e6f61947c4a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.11) >= 0.11.0
Requires:       crate(keccak-0.2/default) >= 0.2.0
Requires:       crate(sponge-cursor-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "shake"

%package     -n %{name}+alloc
Summary:        The SHAKE family of extendable-output functions (XOFs) - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/alloc) >= 0.11.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust shake crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+zeroize
Summary:        The SHAKE family of extendable-output functions (XOFs) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/zeroize) >= 0.11.0
Requires:       crate(sponge-cursor-0.1/zeroize) >= 0.1.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust shake crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
