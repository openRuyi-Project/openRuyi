# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ssh-cipher
%global full_version 0.2.0
%global pkgname ssh-cipher-0.2

Name:           rust-ssh-cipher-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "ssh-cipher"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/SSH/tree/master/ssh-cipher
#!RemoteAsset:  sha256:caac132742f0d33c3af65bfcde7f6aa8f62f0e991d80db99149eb9d44708784f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.4/default) >= 0.4.0
Requires:       crate(ssh-encoding-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
Source code for takopackized Rust crate "ssh-cipher"

%package     -n %{name}+aes-cbc
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "aes-cbc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.8) >= 0.8.0
Requires:       crate(cbc-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/aes-cbc) = %{version}

%description -n %{name}+aes-cbc
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "aes-cbc" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aes-ctr
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "aes-ctr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.8) >= 0.8.0
Requires:       crate(ctr-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/aes-ctr) = %{version}

%description -n %{name}+aes-ctr
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "aes-ctr" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aes-gcm
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "aes-gcm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.8) >= 0.8.0
Requires:       crate(aes-gcm-0.10/aes) >= 0.10.0
Provides:       crate(%{pkgname}/aes-gcm) = %{version}

%description -n %{name}+aes-gcm
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "aes-gcm" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chacha20poly1305
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "chacha20poly1305"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chacha20-0.9) >= 0.9.0
Requires:       crate(poly1305-0.8) >= 0.8.0
Requires:       crate(subtle-2) >= 2.0.0
Provides:       crate(%{pkgname}/chacha20poly1305) = %{version}

%description -n %{name}+chacha20poly1305
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "chacha20poly1305" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tdes
Summary:        Pure Rust implementation of SSH symmetric encryption including support for the modern aes128-gcm@openssh.com/aes256-gcm@openssh.com and chacha20-poly1305@openssh.com algorithms as well as legacy support for older ciphers - feature "tdes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cbc-0.1/default) >= 0.1.0
Requires:       crate(des-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/tdes) = %{version}

%description -n %{name}+tdes
Built on the pure Rust cryptography implementations maintained by the RustCrypto organization.
This metapackage enables feature "tdes" for the Rust ssh-cipher crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
