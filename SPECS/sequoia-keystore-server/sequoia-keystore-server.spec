# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-keystore-server
Version:        0.2.1
Release:        %autorelease
Summary:        Sequoia OpenPGP keystore daemon
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-keystore
#!RemoteAsset:  sha256:d6f0a28a24b299d3c620014ab7b24cf814f08b25310bd4de04271d1dca5aaedc
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  capnproto >= 0.5.2
BuildRequires:  pkgconfig(nettle)
BuildRequires:  clang
BuildRequires:  help2man
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1/default) >= 1.0.18
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/env) >= 4.0.0
BuildRequires:  crate(clap-4/string) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(dirs-5/default) >= 5.0.0
BuildRequires:  crate(sequoia-directories-0.1/default) >= 0.1.0
BuildRequires:  crate(sequoia-ipc-0.36) >= 0.36.0
BuildRequires:  crate(sequoia-keystore-0.7/default) >= 0.7.0
BuildRequires:  crate(sequoia-openpgp-2) >= 2.0.0
# Additional dependencies required by OBS builds.
BuildRequires:  crate(aes-0.8) >= 0.8.4
BuildRequires:  crate(aes-gcm-0.10) >= 0.10.3
BuildRequires:  crate(block-padding-0.3) >= 0.3.3
BuildRequires:  crate(blowfish-0.9) >= 0.9.1
BuildRequires:  crate(botan-0.10) >= 0.10.7
BuildRequires:  crate(camellia-0.1) >= 0.1.0
BuildRequires:  crate(cast5-0.11) >= 0.11.1
BuildRequires:  crate(cbc-0.1) >= 0.1.2
BuildRequires:  crate(cfb-mode-0.8) >= 0.8.2
BuildRequires:  crate(ctor-1) >= 1.0.7
BuildRequires:  crate(cx448-0.1) >= 0.1.1
BuildRequires:  crate(des-0.8) >= 0.8.1
BuildRequires:  crate(dsa-0.6) >= 0.6.3
BuildRequires:  crate(eax-0.5) >= 0.5.0
BuildRequires:  crate(ecb-0.1) >= 0.1.2
BuildRequires:  crate(ecdsa-0.16) >= 0.16.9
BuildRequires:  crate(ed25519-2) >= 2.2.3
BuildRequires:  crate(ed25519-dalek-2) >= 2.2.0
BuildRequires:  crate(hkdf-0.12) >= 0.12.4
BuildRequires:  crate(idea-0.5) >= 0.5.1
BuildRequires:  crate(md-5-0.10) >= 0.10.6
BuildRequires:  crate(ml-dsa-0.1) >= 0.1.1
BuildRequires:  crate(ml-kem-0.3) >= 0.3.2
BuildRequires:  crate(sequoia-openpgp-2/crypto-nettle) >= 2.0.0
BuildRequires:  crate(ocb3-0.1) >= 0.1.0
BuildRequires:  crate(openssl-sys-0.9) >= 0.9.117
BuildRequires:  crate(ossl-1) >= 1.5.3
BuildRequires:  crate(p256-0.13) >= 0.13.2
BuildRequires:  crate(p384-0.13) >= 0.13.1
BuildRequires:  crate(p521-0.13) >= 0.13.3
BuildRequires:  crate(rand-0.10) >= 0.10.1
BuildRequires:  crate(ripemd-0.1) >= 0.1.3
BuildRequires:  crate(rsa-0.9) >= 0.9.10
BuildRequires:  crate(slh-dsa-0.0.3) >= 0.0.3
BuildRequires:  crate(twofish-0.7) >= 0.7.1
BuildRequires:  crate(x25519-dalek-2) >= 2.0.1
BuildRequires:  crate(win-crypto-ng-0.5) >= 0.5.1
BuildRequires:  crate(link-section-0.18) >= 0.18.2
BuildRequires:  crate(linktime-proc-macro-0.2) >= 0.2.0
BuildRequires:  crate(getrandom-0.4) >= 0.4.2
BuildRequires:  crate(zeroize-derive-1) >= 1.4.2
BuildRequires:  crate(annotate-snippets-0.11) >= 0.11.5

Recommends:     gnupg

%description
Sequoia keystore daemon.

%build -p
export PREFIX=%{_prefix}
export ASSET_OUT_DIR="$PWD/assets"

%build -a
help2man --no-info --version-string=%{version} --name='Sequoia OpenPGP keystore daemon' --output=sequoia-keystore.1 target/release/sequoia-keystore

%check -p
export PREFIX=%{_prefix}
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"

%install
install -Dm0755 target/release/sequoia-keystore %{buildroot}%{_libexecdir}/sequoia/sequoia-keystore
install -Dm0644 sequoia-keystore.1 %{buildroot}%{_mandir}/man1/sequoia-keystore.1

%files
%doc README.md
%license LICENSE.txt
%{_libexecdir}/sequoia/
%{_mandir}/man1/sequoia-keystore.1*

%changelog
%autochangelog
