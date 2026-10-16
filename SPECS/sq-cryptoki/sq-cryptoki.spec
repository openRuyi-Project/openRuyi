# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sq-cryptoki
Version:        0.2.0
Release:        %autorelease
Summary:        OpenPGP operations using PKCS#11 tokens
License:        LGPL-2.0-or-later AND CC-BY-4.0
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-cryptoki
#!RemoteAsset:  sha256:894f10b56967a7577c618a7538a03c26e5b2019ad0ec071a8352d82a281f220a
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  capnproto
BuildRequires:  softhsm
BuildRequires:  clang
BuildRequires:  pkgconfig(hogweed)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  help2man
BuildRequires:  crate(anyhow-1/default) >= 1.0.18
BuildRequires:  crate(assert-cmd-2/default) >= 2.0.0
BuildRequires:  crate(chrono-0.4/default) >= 0.4.38
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/env) >= 4.0.0
BuildRequires:  crate(clap-4/string) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(clap-lex-1) >= 1.1.0
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(pastey-0.2/default) >= 0.2.0
BuildRequires:  crate(rpassword-7/default) >= 7.0.0
BuildRequires:  crate(sequoia-cert-store-0.7/default) >= 0.7.0
BuildRequires:  crate(sequoia-cryptoki-0.2/default) >= 0.2.0
BuildRequires:  crate(sequoia-directories-0.1/default) >= 0.1.0
BuildRequires:  crate(sequoia-keystore-0.7/default) >= 0.7.0
BuildRequires:  crate(sequoia-openpgp-2/crypto-nettle) >= 2.4.0
BuildRequires:  crate(sequoia-openpgp-2/default) >= 2.4.0
BuildRequires:  crate(sequoia-openpgp-2/implicit-crypto-backend-for-tests) >= 2.4.0
BuildRequires:  crate(sequoia-policy-config-0.8/default) >= 0.8.0
BuildRequires:  crate(tempfile-3/default) >= 3.1.0
BuildRequires:  crate(terminal-size-0.4/default) >= 0.4.4
BuildRequires:  crate(textwrap-0.16/default) >= 0.16.2
BuildRequires:  crate(aes-gcm-0.10) >= 0.10.3
BuildRequires:  crate(cx448-0.1) >= 0.1.1
BuildRequires:  crate(eax-0.5) >= 0.5.0
BuildRequires:  crate(ed25519-2) >= 2.2.3
BuildRequires:  crate(ed25519-dalek-2) >= 2.2.0
BuildRequires:  crate(hkdf-0.12) >= 0.12.4
BuildRequires:  crate(num-bigint-dig-0.8) >= 0.8.6
BuildRequires:  crate(ocb3-0.1) >= 0.1.0
BuildRequires:  crate(win-crypto-ng-0.5) >= 0.5.1
BuildRequires:  crate(aes-0.8) >= 0.8.4
BuildRequires:  crate(block-padding-0.3) >= 0.3.3

%description
Tool for working with PKCS#11 devices (cryptokis) from Sequoia.

%build -p
export ASSET_OUT_DIR="$PWD/assets"

%build -a
help2man --no-info --version-string=%{version} --name='OpenPGP operations using PKCS#11 tokens' --output=sq-cryptoki.1 target/release/sq-cryptoki

%check -p
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"
export SEQUOIA_CRYPTOKI_BACKEND=softhsm2
export SEQUOIA_CRYPTOKI_MODULE=%{_libdir}/pkcs11/libsofthsm2.so

%install
install -Dm0755 target/release/sq-cryptoki %{buildroot}%{_bindir}/sq-cryptoki
install -Dm0644 sq-cryptoki.1 %{buildroot}%{_mandir}/man1/sq-cryptoki.1

%files
%doc README.md
%license LICENSE-CC-BY-4.0.txt LICENSE-LGPL-2.0.txt LICENSE.txt
%{_bindir}/sq-cryptoki
%{_mandir}/man1/sq-cryptoki.1*

%changelog
%autochangelog
