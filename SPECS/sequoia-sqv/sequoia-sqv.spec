# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-sqv
Version:        1.5.0
Release:        %autorelease
Summary:        Simple OpenPGP signature verification
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-sqv
#!RemoteAsset:  sha256:d4eb1f22746894dd654a8fa50576200d047f0de0e1ae2a361d7ebe263d351bc8
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(nettle)
BuildRequires:  clang
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1) >= 1.0.18
BuildRequires:  crate(anyhow-1/default) >= 1.0.18
BuildRequires:  crate(chrono-0.4) >= 0.4.10
BuildRequires:  crate(chrono-0.4/default) >= 0.4.10
BuildRequires:  crate(clap-4) >= 4.0.0
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/string) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(clap-complete-4) >= 4.0.0
BuildRequires:  crate(sequoia-man-0.3) >= 0.3.0
BuildRequires:  crate(sequoia-openpgp-2) >= 2.4.0
BuildRequires:  crate(sequoia-openpgp-2/compression) >= 2.4.0
BuildRequires:  crate(sequoia-policy-config-0.8) >= 0.8.0
BuildRequires:  crate(sequoia-policy-config-0.8/default) >= 0.8.0
# Additional dependencies required by OBS builds.
BuildRequires:  crate(assert-cmd-2/default) >= 2.0.0
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
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
BuildRequires:  crate(sequoia-openpgp-2/crypto-nettle) >= 2.4.0
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
BuildRequires:  crate(predicates-3/default) >= 3.0.0
BuildRequires:  crate(link-section-0.18) >= 0.18.2
BuildRequires:  crate(linktime-proc-macro-0.2) >= 0.2.0
BuildRequires:  crate(getrandom-0.4) >= 0.4.2
BuildRequires:  crate(zeroize-derive-1) >= 1.4.2
BuildRequires:  crate(annotate-snippets-0.11) >= 0.11.5

%description
A simple OpenPGP signature verification program.

%build -p
export ASSET_OUT_DIR="$PWD/assets"

%check -p
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"

%install
install -Dm0755 target/release/sqv %{buildroot}%{_bindir}/sqv
install -d %{buildroot}%{_mandir}/man1
install -m0644 assets/man-pages/*.1 %{buildroot}%{_mandir}/man1/
install -Dm0644 assets/shell-completions/sqv.bash %{buildroot}%{bash_completions_dir}/sqv
install -Dm0644 assets/shell-completions/_sqv %{buildroot}%{_datadir}/zsh/site-functions/_sqv
install -Dm0644 assets/shell-completions/sqv.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sqv.fish

%files
%doc README.md NEWS openpgp-policy.toml
%license LICENSE.txt
%{_bindir}/sqv
%{_mandir}/man1/*
%{bash_completions_dir}/sqv
%{_datadir}/zsh/site-functions/_sqv
%{_datadir}/fish/vendor_completions.d/sqv.fish

%changelog
%autochangelog
