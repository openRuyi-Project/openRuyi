# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cipher
%global full_version 0.4.4
%global pkgname cipher-0.4

Name:           rust-cipher-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "cipher"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:773f3b9af64447d2ce9850330c473515014aa235e6a783b02db81ff39e4a3dad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.1/default) >= 0.1.6
Requires:       crate(inout-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cipher"

%package     -n %{name}+blobby
Summary:        Traits for describing block ciphers and stream ciphers - feature "blobby" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(blobby-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/blobby) = %{version}
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev" feature.

%package     -n %{name}+block-padding
Summary:        Traits for describing block ciphers and stream ciphers - feature "block-padding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(inout-0.1/block-padding) >= 0.1.0
Provides:       crate(%{pkgname}/block-padding) = %{version}

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for describing block ciphers and stream ciphers - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.1/rand-core) >= 0.1.6
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Traits for describing block ciphers and stream ciphers - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(crypto-common-0.1/std) >= 0.1.6
Requires:       crate(inout-0.1/std) >= 0.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Traits for describing block ciphers and stream ciphers - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.5.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
