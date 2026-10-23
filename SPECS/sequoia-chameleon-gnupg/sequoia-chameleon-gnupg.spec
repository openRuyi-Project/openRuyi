# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-chameleon-gnupg
Version:        0.13.1
Release:        %autorelease
Summary:        GnuPG-compatible commands implemented with Sequoia
License:        GPL-3.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-chameleon-gnupg
#!RemoteAsset:  sha256:709cc7440fe79a0794209c82e48fe5044358f1e37d11bb9a4a27ebe64fb6eae2
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  clang
BuildRequires:  capnproto >= 0.5.2
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  libfaketime
BuildRequires:  tzdata
BuildRequires:  sequoia-sq
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1) >= 1.0.0
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(base64-0.21/default) >= 0.21.0
BuildRequires:  crate(buffered-reader-1/default) >= 1.4.0
BuildRequires:  crate(chrono-0.4/default) >= 0.4.0
BuildRequires:  crate(clap-4) >= 4.4.18
BuildRequires:  crate(clap-complete-4) >= 4.4.9
BuildRequires:  crate(clap-mangen-0.2) >= 0.2.19
BuildRequires:  crate(daemonize-0.5/default) >= 0.5.0
BuildRequires:  crate(dirs-5/default) >= 5.0.0
BuildRequires:  crate(fd-lock-3) >= 3.0.0
BuildRequires:  crate(filetime-0.2/default) >= 0.2.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.0
BuildRequires:  crate(indexmap-2/default) >= 2.0.0
BuildRequires:  crate(interprocess-1) >= 1.0.0
BuildRequires:  crate(libc-0.2) >= 0.2.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(memchr-2/default) >= 2.0.0
BuildRequires:  crate(openssh-keys-0.6) >= 0.6.0
BuildRequires:  crate(percent-encoding-2/default) >= 2.0.0
BuildRequires:  crate(rand-0.8/default) >= 0.8.0
BuildRequires:  crate(rand-distr-0.4) >= 0.4.0
BuildRequires:  crate(rayon-1/default) >= 1.0.0
BuildRequires:  crate(reqwest-0.12/default) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/socks) >= 0.12.0
BuildRequires:  crate(roff-0.2) >= 0.2.0
BuildRequires:  crate(rpassword-7/default) >= 7.0.0
BuildRequires:  crate(rusqlite-0.29/default) >= 0.29.0
BuildRequires:  crate(sequoia-cert-store-0.7) >= 0.7.0
BuildRequires:  crate(sequoia-gpg-agent-0.6) >= 0.6.0
BuildRequires:  crate(sequoia-ipc-0.36) >= 0.36.0
BuildRequires:  crate(sequoia-net-0.30) >= 0.30.0
BuildRequires:  crate(sequoia-openpgp-2/compression) >= 2.0.0
BuildRequires:  crate(sequoia-policy-config-0.8) >= 0.8.0
BuildRequires:  crate(sequoia-wot-0.14) >= 0.14.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(shellexpand-3/default) >= 3.0.0
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
BuildRequires:  crate(thiserror-1) >= 1.0.0
BuildRequires:  crate(thiserror-1/default) >= 1.0.0
BuildRequires:  crate(tokio-1/default) >= 1.19.0
BuildRequires:  crate(tokio-1/fs) >= 1.19.0
BuildRequires:  crate(tokio-1/io-std) >= 1.19.0
BuildRequires:  crate(tokio-1/io-util) >= 1.19.0
BuildRequires:  crate(tokio-1/net) >= 1.19.0
BuildRequires:  crate(tokio-1/process) >= 1.19.0
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.19.0
# Additional dependencies required by OBS builds.
BuildRequires:  crate(editdistancek-1/default) >= 1.0.0
BuildRequires:  crate(histo-1/default) >= 1.0.0
BuildRequires:  crate(ntest-0.9/default) >= 0.9.0
BuildRequires:  crate(pty-process-0.4) >= 0.4.0
BuildRequires:  crate(serde-with-3/default) >= 3.0.0
BuildRequires:  crate(tar-0.4) >= 0.4.0
BuildRequires:  crate(aes-gcm-0.10) >= 0.10.3
BuildRequires:  crate(botan-0.10) >= 0.10.7
BuildRequires:  crate(ctor-1) >= 1.0.7
BuildRequires:  crate(cx448-0.1) >= 0.1.1
BuildRequires:  crate(eax-0.5) >= 0.5.0
BuildRequires:  crate(ed25519-2) >= 2.2.3
BuildRequires:  crate(ed25519-dalek-2) >= 2.2.0
BuildRequires:  crate(hkdf-0.12) >= 0.12.4
BuildRequires:  crate(sequoia-openpgp-2/crypto-nettle) >= 2.0.0
BuildRequires:  crate(num-bigint-dig-0.8) >= 0.8.6
BuildRequires:  crate(ocb3-0.1) >= 0.1.0
BuildRequires:  crate(ossl-1) >= 1.5.3
BuildRequires:  crate(win-crypto-ng-0.5) >= 0.5.1
BuildRequires:  crate(aes-0.8) >= 0.8.4
BuildRequires:  crate(link-section-0.18) >= 0.18.2
BuildRequires:  crate(linktime-proc-macro-0.2) >= 0.2.0
BuildRequires:  crate(clap-4/default) >= 4.4.18
BuildRequires:  crate(block-padding-0.3) >= 0.3.3
BuildRequires:  crate(prettyplease-0.2) >= 0.2.37
BuildRequires:  crate(annotate-snippets-0.11) >= 0.11.5

Requires:       gnupg

%description
Sequoia's reimplementation of the GnuPG interface.

%build -p
export ASSET_OUT_DIR="$PWD/assets"

%check -p
# Cached integration-test keys were created in 2022 with a three-year lifetime.
export LD_PRELOAD=%{_libdir}/libfaketime.so.1
export FAKETIME="@2024-05-16 12:00:00"
export FAKETIME_DONT_FAKE_MONOTONIC=1
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"

%install
install -Dm0755 target/release/gpg-sq %{buildroot}%{_bindir}/gpg-sq
install -Dm0755 target/release/gpgv-sq %{buildroot}%{_bindir}/gpgv-sq
install -d %{buildroot}%{_mandir}/man1
install -m0644 assets/man-pages/*.1 %{buildroot}%{_mandir}/man1/
install -Dm0644 assets/shell-completions/gpg-sq.bash %{buildroot}%{bash_completions_dir}/gpg-sq
install -Dm0644 assets/shell-completions/_gpg-sq %{buildroot}%{_datadir}/zsh/site-functions/_gpg-sq
install -Dm0644 assets/shell-completions/gpg-sq.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/gpg-sq.fish
install -Dm0644 assets/shell-completions/gpgv-sq.bash %{buildroot}%{bash_completions_dir}/gpgv-sq
install -Dm0644 assets/shell-completions/_gpgv-sq %{buildroot}%{_datadir}/zsh/site-functions/_gpgv-sq
install -Dm0644 assets/shell-completions/gpgv-sq.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/gpgv-sq.fish

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/gpg-sq
%{_bindir}/gpgv-sq
%{_mandir}/man1/*
%{bash_completions_dir}/gpg-sq
%{_datadir}/zsh/site-functions/_gpg-sq
%{_datadir}/fish/vendor_completions.d/gpg-sq.fish
%{bash_completions_dir}/gpgv-sq
%{_datadir}/zsh/site-functions/_gpgv-sq
%{_datadir}/fish/vendor_completions.d/gpgv-sq.fish

%changelog
%autochangelog
