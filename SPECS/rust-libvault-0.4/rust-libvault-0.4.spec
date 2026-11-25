# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libvault
%global full_version 0.4.0
%global pkgname libvault-0.4

Name:           rust-libvault-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "libvault"
License:        MIT OR Apache-2.0
URL:            https://github.com/gitmono-dev/libvault-rs
#!RemoteAsset:  sha256:50f3a707f5446189c7ba3af2a9f36bfe68ee3ad0e1c74e017e2f2fb06750ffa3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.104
Requires:       crate(arc-swap-1/default) >= 1.9.2
Requires:       crate(as-any-0.3/default) >= 0.3.2
Requires:       crate(async-trait-0.1/default) >= 0.1.92
Requires:       crate(base64-0.22/alloc) >= 0.22.1
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(bcrypt-0.19/default) >= 0.19.3
Requires:       crate(better-default-1/default) >= 1.0.5
Requires:       crate(blake2b-simd-1/default) >= 1.0.5
Requires:       crate(blake3-1/default) >= 1.8.7
Requires:       crate(builder-pattern-0.4/default) >= 0.4.2
Requires:       crate(chrono-0.4/default) >= 0.4.45
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.16
Requires:       crate(daemonize-0.5/default) >= 0.5.0
Requires:       crate(dashmap-7.0.0-rc2/default) >= 7.0.0-rc2
Requires:       crate(derivative-2/default) >= 2.2.0
Requires:       crate(derive-more-2/default) >= 2.1.1
Requires:       crate(derive-more-2/full) >= 2.1.1
Requires:       crate(enum-map-3/default) >= 3.1.0
Requires:       crate(foreign-types-0.3/default) >= 0.3.2
Requires:       crate(glob-0.3/default) >= 0.3.4
Requires:       crate(go-defer-0.1/default) >= 0.1.0
Requires:       crate(hcl-rs-0.19/default) >= 0.19.8
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(humantime-2/default) >= 2.4.0
Requires:       crate(ipnetwork-0.21/default) >= 0.21.1
Requires:       crate(ipnetwork-0.21/serde) >= 0.21.1
Requires:       crate(itertools-0.15/default) >= 0.15.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(libc-0.2/default) >= 0.2.189
Requires:       crate(lockfile-0.4/default) >= 0.4.0
Requires:       crate(log-0.4/default) >= 0.4.33
Requires:       crate(pem-4/default) >= 4.0.0
Requires:       crate(pgp-0.20/default) >= 0.20.0
Requires:       crate(priority-queue-2/default) >= 2.7.0
Requires:       crate(radix-trie-0.3/default) >= 0.3.0
Requires:       crate(rand-0.10/default) >= 0.10.2
Requires:       crate(rand-chacha-0.3/default) >= 0.3.1
Requires:       crate(regex-1/default) >= 1.13.1
Requires:       crate(reqwest-0.13/default) >= 0.13.5
Requires:       crate(reqwest-0.13/json) >= 0.13.5
Requires:       crate(reqwest-0.13/rustls) >= 0.13.5
Requires:       crate(rustls-0.24.0-dev.1/default) >= 0.24.0-dev.1
Requires:       crate(rustls-pemfile-2/default) >= 2.2.0
Requires:       crate(rustls-webpki-0.104.0-alpha.7/default) >= 0.104.0-alpha.7
Requires:       crate(serde-1/alloc) >= 1.0.229
Requires:       crate(serde-1/default) >= 1.0.229
Requires:       crate(serde-1/derive) >= 1.0.229
Requires:       crate(serde-1/rc) >= 1.0.229
Requires:       crate(serde-bytes-0.11/default) >= 0.11.19
Requires:       crate(serde-derive-1/default) >= 1.0.229
Requires:       crate(serde-json-1/default) >= 1.0.151
Requires:       crate(serde-yaml-0.9/default) >= 0.9.33
Requires:       crate(smallvec-1/default) >= 1.16.1
Requires:       crate(ssh-key-0.7.0-rc.11/crypto) >= 0.7.0-rc.11
Requires:       crate(ssh-key-0.7.0-rc.11/default) >= 0.7.0-rc.11
Requires:       crate(ssh-key-0.7.0-rc.11/getrandom) >= 0.7.0-rc.11
Requires:       crate(ssh-key-0.7.0-rc.11/std) >= 0.7.0-rc.11
Requires:       crate(stretto-0.9/default) >= 0.9.0
Requires:       crate(strum-0.28/default) >= 0.28.0
Requires:       crate(strum-0.28/derive) >= 0.28.0
Requires:       crate(strum-macros-0.28/default) >= 0.28.0
Requires:       crate(tempfile-3/default) >= 3.27.0
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(tokio-1/default) >= 1.53.1
Requires:       crate(tokio-1/macros) >= 1.53.1
Requires:       crate(tokio-1/rt-multi-thread) >= 1.53.1
Requires:       crate(toml-1) >= 1.1.6
Requires:       crate(tonic-0.14/default) >= 0.14.6
Requires:       crate(tracing-0.1/default) >= 0.1.44
Requires:       crate(ureq-3/default) >= 3.4.1
Requires:       crate(ureq-3/json) >= 3.4.1
Requires:       crate(url-2/default) >= 2.5.8
Requires:       crate(webpki-roots-1/default) >= 1.0.9
Requires:       crate(x509-parser-0.18/default) >= 0.18.1
Requires:       crate(zeroize-1/default) >= 1.9.0
Requires:       crate(zeroize-1/zeroize-derive) >= 1.9.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "libvault"

%package     -n %{name}+crypto-adaptor-openssl
Summary:        Libvault is modified from RustyVault - feature "crypto_adaptor_openssl" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-0.10/default) >= 0.10.81
Requires:       crate(openssl-sys-0.9/default) >= 0.9.117
Provides:       crate(%{pkgname}/crypto-adaptor-openssl) = %{version}
Provides:       crate(%{pkgname}/crypto-adaptor-tongsuo) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+crypto-adaptor-openssl
This metapackage enables feature "crypto_adaptor_openssl" for the Rust libvault crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "crypto_adaptor_tongsuo", and "default" features.

%package     -n %{name}+etcd-client
Summary:        Libvault is modified from RustyVault - feature "etcd-client" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(etcd-client-0.20/default) >= 0.20.0
Requires:       crate(etcd-client-0.20/tls) >= 0.20.0
Provides:       crate(%{pkgname}/etcd-client) = %{version}
Provides:       crate(%{pkgname}/storage-xline) = %{version}

%description -n %{name}+etcd-client
This metapackage enables feature "etcd-client" for the Rust libvault crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "storage_xline" feature.

%package     -n %{name}+sqlx
Summary:        Libvault is modified from RustyVault - feature "sqlx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/default) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx) = %{version}

%description -n %{name}+sqlx
This metapackage enables feature "sqlx" for the Rust libvault crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+storage-pg
Summary:        Libvault is modified from RustyVault - feature "storage_pg"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/postgres) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/storage-pg) = %{version}

%description -n %{name}+storage-pg
This metapackage enables feature "storage_pg" for the Rust libvault crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+storage-sqlite
Summary:        Libvault is modified from RustyVault - feature "storage_sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Requires:       crate(sqlx-0.9/sqlite) >= 0.9.0
Provides:       crate(%{pkgname}/storage-sqlite) = %{version}

%description -n %{name}+storage-sqlite
This metapackage enables feature "storage_sqlite" for the Rust libvault crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
