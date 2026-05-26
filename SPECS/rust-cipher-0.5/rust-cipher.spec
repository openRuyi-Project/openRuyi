# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cipher
%global full_version 0.5.1
%global pkgname cipher-0.5

Name:           rust-cipher-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "cipher"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:e34d8227fe1ba289043aeb13792056ff80fd6de1a9f49137a5f499de8e8c78ea
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.2/default) >= 0.2.1
Requires:       crate(inout-0.2/default) >= 0.2.2
Provides:       crate(cipher) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cipher"

%package     -n %{name}+blobby
Summary:        Traits for describing block ciphers and stream ciphers - feature "blobby" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(blobby-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/blobby)
Provides:       crate(%{pkgname}/dev)

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev" feature.

%package     -n %{name}+block-buffer
Summary:        Traits for describing block ciphers and stream ciphers - feature "block-buffer" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(block-buffer-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/block-buffer)
Provides:       crate(%{pkgname}/stream-wrapper)

%description -n %{name}+block-buffer
This metapackage enables feature "block-buffer" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "stream-wrapper" feature.

%package     -n %{name}+block-padding
Summary:        Traits for describing block ciphers and stream ciphers - feature "block-padding"
Requires:       crate(%{pkgname})
Requires:       crate(inout-0.2/block-padding) >= 0.2.2
Provides:       crate(%{pkgname}/block-padding)

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Traits for describing block ciphers and stream ciphers - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(crypto-common-0.2/getrandom) >= 0.2.1
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for describing block ciphers and stream ciphers - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.1
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Traits for describing block ciphers and stream ciphers - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(block-buffer-0.12/zeroize) >= 0.12.0
Requires:       crate(crypto-common-0.2/zeroize) >= 0.2.1
Requires:       crate(zeroize-1.0) >= 1.8
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust cipher crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
