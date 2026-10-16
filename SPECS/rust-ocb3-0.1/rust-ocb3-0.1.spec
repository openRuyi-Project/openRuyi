# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ocb3
%global full_version 0.1.0
%global pkgname ocb3-0.1

Name:           rust-ocb3-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ocb3"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/AEADs
#!RemoteAsset:  sha256:c196e0276c471c843dd5777e7543a36a298a4be942a2a688d8111cd43390dedb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aead-0.5) >= 0.5.0
Requires:       crate(cipher-0.4/default) >= 0.4.0
Requires:       crate(ctr-0.9/default) >= 0.9.0
Requires:       crate(subtle-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ocb3"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/alloc) >= 0.5.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrayvec
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "arrayvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/arrayvec) >= 0.5.0
Provides:       crate(%{pkgname}/arrayvec) = %{version}

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(aead-0.5/getrandom) >= 0.5.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapless
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "heapless"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/heapless) >= 0.5.0
Provides:       crate(%{pkgname}/heapless) = %{version}

%description -n %{name}+heapless
This metapackage enables feature "heapless" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/rand-core) >= 0.5.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(aead-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/stream) >= 0.5.0
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Offset Codebook Mode v3 (OCB3) Authenticated Encryption with Associated Data (AEAD) Cipher as described in RFC7253 - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ocb3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
