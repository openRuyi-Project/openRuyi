# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-git
Version:        0.6.0
Release:        %autorelease
Summary:        OpenPGP signing and verification for Git
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-git
#!RemoteAsset:  sha256:068f0729a562ce45ed472171af24c0a5ece79cf56e84a756ac1f4a143fd38947
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  clang
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  libfaketime
BuildRequires:  git-core
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1) >= 1.0.0
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(buffered-reader-1/default) >= 1.4.0
BuildRequires:  crate(clap-4) >= 4.0.0
BuildRequires:  crate(clap-4/cargo) >= 4.0.0
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/env) >= 4.0.0
BuildRequires:  crate(clap-4/string) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(clap-complete-4) >= 4.0.0
BuildRequires:  crate(clap-mangen-0.2) >= 0.2.0
BuildRequires:  crate(dirs-5) >= 5.0.0
BuildRequires:  crate(dirs-5/default) >= 5.0.0
BuildRequires:  crate(git2-0.19) >= 0.19.0
BuildRequires:  crate(once-cell-1/default) >= 1.0.0
BuildRequires:  crate(roff-0.2) >= 0.2.0
BuildRequires:  crate(sequoia-cert-store-0.7) >= 0.7.0
BuildRequires:  crate(sequoia-directories-0.1) >= 0.1.0
BuildRequires:  crate(sequoia-directories-0.1/default) >= 0.1.0
BuildRequires:  crate(sequoia-man-0.3) >= 0.3.0
BuildRequires:  crate(sequoia-net-0.30/default) >= 0.30.0
BuildRequires:  crate(sequoia-openpgp-2/default) >= 2.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(tempfile-3/default) >= 3.20.0
BuildRequires:  crate(thiserror-1/default) >= 1.0.0
BuildRequires:  crate(tokio-1/default) >= 1.0.0
BuildRequires:  crate(tokio-1/full) >= 1.0.0
BuildRequires:  crate(toml-0.8/default) >= 0.8.0

%description
A tool for managing and enforcing a commit signing policy.

%build -p
export ASSET_OUT_DIR="$PWD/assets"

%check -p
# The faketime wrapper in the build root duplicates /usr in its library path.
export FAKETIME_DISABLE_SHM=1
export FAKETIME_DONT_FAKE_MONOTONIC=1
export LD_PRELOAD=%{_libdir}/libfaketime.so.1
test "$(faketime -f '2000-01-01 00:00:00' date -u +%%Y)" = 2000
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"

%install
install -Dm0755 target/release/sq-git %{buildroot}%{_bindir}/sq-git
install -d %{buildroot}%{_mandir}/man1
install -m0644 assets/man-pages/*.1 %{buildroot}%{_mandir}/man1/
install -Dm0644 assets/shell-completions/sq-git.bash %{buildroot}%{bash_completions_dir}/sq-git
install -Dm0644 assets/shell-completions/_sq-git %{buildroot}%{_datadir}/zsh/site-functions/_sq-git
install -Dm0644 assets/shell-completions/sq-git.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sq-git.fish

%files
%doc README.md NEWS openpgp-policy.toml
%license LICENSE.txt
%{_bindir}/sq-git
%{_mandir}/man1/*
%{bash_completions_dir}/sq-git
%{_datadir}/zsh/site-functions/_sq-git
%{_datadir}/fish/vendor_completions.d/sq-git.fish

%changelog
%autochangelog
