# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ssh-cipher
%global full_version 0.3.0
%global pkgname ssh-cipher-0.3

Name:           rust-ssh-cipher-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "ssh-cipher"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/SSH/tree/master/ssh-cipher
#!RemoteAsset:  sha256:d801accda99469cde6d73da741422610fdf6508a72d9a69d1b55cb241c720597
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
Source code for takopackized Rust crate "ssh-cipher"

%package     -n %{name}+aes
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "aes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.6) >= 0.6.0
Requires:       crate(aes-0.9) >= 0.9.0
Requires:       crate(aes-gcm-0.11/aes) >= 0.11.0
Provides:       crate(%{pkgname}/aes) = %{version}

%description -n %{name}+aes
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "aes" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chacha20poly1305
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "chacha20poly1305"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.6) >= 0.6.0
Requires:       crate(chacha20-0.10/cipher) >= 0.10.0
Requires:       crate(chacha20-0.10/legacy) >= 0.10.0
Requires:       crate(ctutils-0.4) >= 0.4.0
Requires:       crate(poly1305-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/chacha20poly1305) = %{version}

%description -n %{name}+chacha20poly1305
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "chacha20poly1305" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "encoding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ssh-encoding-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/encoding) = %{version}

%description -n %{name}+encoding
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "encoding" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(aead-0.6/getrandom) >= 0.6.0
Requires:       crate(cipher-0.5/getrandom) >= 0.5.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "getrandom" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.6/rand-core) >= 0.6.0
Requires:       crate(cipher-0.5/rand-core) >= 0.5.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "rand_core" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tdes
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "tdes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(des-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/tdes) = %{version}

%description -n %{name}+tdes
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "tdes" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.9/zeroize) >= 0.9.0
Requires:       crate(aes-gcm-0.11/aes) >= 0.11.0
Requires:       crate(aes-gcm-0.11/zeroize) >= 0.11.0
Requires:       crate(chacha20-0.10/cipher) >= 0.10.0
Requires:       crate(chacha20-0.10/legacy) >= 0.10.0
Requires:       crate(chacha20-0.10/zeroize) >= 0.10.0
Requires:       crate(des-0.9/zeroize) >= 0.9.0
Requires:       crate(poly1305-0.9/zeroize) >= 0.9.0
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "zeroize" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
