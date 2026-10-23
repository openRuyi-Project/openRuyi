# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-sq
Version:        1.5.0
Release:        %autorelease
Summary:        Command-line tools for OpenPGP
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-sq
#!RemoteAsset:  sha256:43f230abc78a8daec8a06cfc8c1191045b7b210fee5bee50dc3f75bd9f22950e
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  clang
BuildRequires:  capnproto >= 0.5.2
BuildRequires:  pkgconfig(sqlite3)
# TakoPack-generated dependencies.
BuildRequires:  crate(aho-corasick-1/default) >= 1.0.0
BuildRequires:  crate(anyhow-1) >= 1.0.18
BuildRequires:  crate(anyhow-1/default) >= 1.0.18
BuildRequires:  crate(cfg-if-1) >= 1.0.0
BuildRequires:  crate(chrono-0.4) >= 0.4.38
BuildRequires:  crate(chrono-0.4/default) >= 0.4.10
BuildRequires:  crate(clap-4) >= 4.0.0
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/env) >= 4.0.0
BuildRequires:  crate(clap-4/string) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(clap-complete-4) >= 4.0.0
BuildRequires:  crate(clap-lex-0.7) >= 0.7.0
BuildRequires:  crate(dirs-5) >= 5.0.0
BuildRequires:  crate(dirs-5/default) >= 5.0.0
BuildRequires:  crate(fs-extra-1/default) >= 1.0.0
BuildRequires:  crate(futures-util-0.3/default) >= 0.3.0
BuildRequires:  crate(indicatif-0.18/default) >= 0.18.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(regex-1/default) >= 1.0.0
BuildRequires:  crate(reqwest-0.12/default) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/hickory-dns) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/stream) >= 0.12.0
BuildRequires:  crate(roff-0.2) >= 0.2.1
BuildRequires:  crate(rpassword-7/default) >= 7.0.0
BuildRequires:  crate(sequoia-man-0.3) >= 0.3.0
BuildRequires:  crate(sequoia-net-0.30) >= 0.30.0
BuildRequires:  crate(sequoia-openpgp-2) >= 2.0.0
BuildRequires:  crate(sequoia-policy-config-0.8/default) >= 0.8.0
BuildRequires:  crate(serde-1) >= 1.0.137
BuildRequires:  crate(serde-1/default) >= 1.0.137
BuildRequires:  crate(serde-1/derive) >= 1.0.137
BuildRequires:  crate(sqz-0.1) >= 0.1.0
BuildRequires:  crate(sqz-0.1/clap) >= 0.1.0
BuildRequires:  crate(sqz-0.1/net) >= 0.1.0
BuildRequires:  crate(tempfile-3/default) >= 3.1.0
BuildRequires:  crate(termcolor-1/default) >= 1.2.0
BuildRequires:  crate(terminal-size-0.2) >= 0.2.6
BuildRequires:  crate(terminal-size-0.2/default) >= 0.2.6
BuildRequires:  crate(textwrap-0.15) >= 0.15.0
BuildRequires:  crate(textwrap-0.15/smawk) >= 0.15.0
BuildRequires:  crate(textwrap-0.15/unicode-width) >= 0.15.0
BuildRequires:  crate(thiserror-1/default) >= 1.0.0
BuildRequires:  crate(tokio-1/default) >= 1.13.1
BuildRequires:  crate(typenum-1) >= 1.0.0
BuildRequires:  crate(typenum-1/default) >= 1.0.0
# Additional dependencies required by OBS builds.
BuildRequires:  crate(culpa-1/default) >= 1.0.2
BuildRequires:  crate(subplotlib-0.12/default) >= 0.12.0
BuildRequires:  crate(assert-cmd-2/default) >= 2.0.0
BuildRequires:  crate(subplot-build-0.12/default) >= 0.12.0
BuildRequires:  crate(predicates-3/default) >= 3.1.4
BuildRequires:  crate(sequoia-openpgp-2/crypto-nettle) >= 2.0.0
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
BuildRequires:  crate(blowfish-0.9) >= 0.9.1
BuildRequires:  crate(botan-0.10) >= 0.10.7
BuildRequires:  crate(camellia-0.1) >= 0.1.0
BuildRequires:  crate(cast5-0.11) >= 0.11.1
BuildRequires:  crate(cbc-0.1) >= 0.1.2
BuildRequires:  crate(cfb-mode-0.8) >= 0.8.2
BuildRequires:  crate(ctor-1) >= 1.0.7
BuildRequires:  crate(des-0.8) >= 0.8.1
BuildRequires:  crate(dsa-0.6) >= 0.6.3
BuildRequires:  crate(ecb-0.1) >= 0.1.2
BuildRequires:  crate(ecdsa-0.16) >= 0.16.9
BuildRequires:  crate(idea-0.5) >= 0.5.1
BuildRequires:  crate(md-5-0.10) >= 0.10.6
BuildRequires:  crate(ml-dsa-0.1) >= 0.1.1
BuildRequires:  crate(ml-kem-0.3) >= 0.3.2
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
BuildRequires:  crate(link-section-0.18) >= 0.18.2
BuildRequires:  crate(linktime-proc-macro-0.2) >= 0.2.0
BuildRequires:  crate(zeroize-derive-1) >= 1.4.2
BuildRequires:  crate(annotate-snippets-0.11) >= 0.11.5

Recommends:     gnupg
Recommends:     sequoia-keystore-server

%description
Command-line frontends for Sequoia.

%build -p
export PREFIX=%{_prefix}
export ASSET_OUT_DIR="$PWD/assets"

%check -p
export PREFIX=%{_prefix}
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"

%install
install -Dm0755 target/release/sq %{buildroot}%{_bindir}/sq
install -d %{buildroot}%{_mandir}/man1
install -m0644 assets/man-pages/*.1 %{buildroot}%{_mandir}/man1/
install -Dm0644 assets/shell-completions/sq.bash %{buildroot}%{bash_completions_dir}/sq
install -Dm0644 assets/shell-completions/_sq %{buildroot}%{_datadir}/zsh/site-functions/_sq
install -Dm0644 assets/shell-completions/sq.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sq.fish

%files
%doc README.md NEWS
%license LICENSE.txt
%{_bindir}/sq
%{_mandir}/man1/*
%{bash_completions_dir}/sq
%{_datadir}/zsh/site-functions/_sq
%{_datadir}/fish/vendor_completions.d/sq.fish

%changelog
%autochangelog
