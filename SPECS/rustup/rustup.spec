# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rustup
Version:        1.29.0
Release:        %autorelease
Summary:        The Rust toolchain installer
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/rustup
#!RemoteAsset:  sha256:de73d1a62f4d5409a2f6bdb1c523d8dc08aa6d9d63588db62493c19ca8f8bf55
Source:         https://github.com/rust-lang/rustup/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildOption(build):  --features no-self-update

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anstream-1/default) >= 1.0.0
BuildRequires:  crate(anstyle-1/default) >= 1.0.11
BuildRequires:  crate(anyhow-1/default) >= 1.0.69
BuildRequires:  crate(cc-1/default) >= 1.0.0
BuildRequires:  crate(cfg-if-1/default) >= 1.0.0
BuildRequires:  crate(chrono-0.4/std) >= 0.4.0
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/string) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(clap-cargo-0.18/default) >= 0.18.3
BuildRequires:  crate(clap-complete-4/default) >= 4.0.0
BuildRequires:  crate(console-0.16/default) >= 0.16.0
BuildRequires:  crate(effective-limits-0.5/default) >= 0.5.5
BuildRequires:  crate(enum-map-2/default) >= 2.5.0
BuildRequires:  crate(flate2-1/zlib-rs) >= 1.1.1
BuildRequires:  crate(fs-at-0.2/default) >= 0.2.1
BuildRequires:  crate(futures-util-0.3/default) >= 0.3.31
BuildRequires:  crate(git-testament-0.2/default) >= 0.2.0
BuildRequires:  crate(home-0.5/default) >= 0.5.4
BuildRequires:  crate(indicatif-0.18/default) >= 0.18.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(opener-0.8/default) >= 0.8.0
BuildRequires:  crate(platforms-3) >= 3.4.0
BuildRequires:  crate(platforms-3/default) >= 3.4.0
BuildRequires:  crate(pulldown-cmark-0.13) >= 0.13.0
BuildRequires:  crate(rand-0.10/default) >= 0.10.0
BuildRequires:  crate(rayon-1/default) >= 1.10.0
BuildRequires:  crate(regex-1/default) >= 1.0.0
BuildRequires:  crate(remove-dir-all-1/default) >= 1.0.0
BuildRequires:  crate(remove-dir-all-1/parallel) >= 1.0.0
BuildRequires:  crate(retry-2/random) >= 2.0.0
BuildRequires:  crate(rs-tracing-1/default) >= 1.1.0
BuildRequires:  crate(rs-tracing-1/rs-tracing) >= 1.1.0
BuildRequires:  crate(same-file-1/default) >= 1.0.0
BuildRequires:  crate(scopeguard-1/default) >= 1.0.0
BuildRequires:  crate(semver-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(sha2-0.10/default) >= 0.10.0
BuildRequires:  crate(sharded-slab-0.1/default) >= 0.1.1
BuildRequires:  crate(strsim-0.11/default) >= 0.11.0
BuildRequires:  crate(tar-0.4/default) >= 0.4.26
BuildRequires:  crate(tempfile-3/default) >= 3.8.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.0
BuildRequires:  crate(threadpool-1/default) >= 1.0.0
BuildRequires:  crate(tokio-1/macros) >= 1.26.0
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.26.0
BuildRequires:  crate(tokio-1/sync) >= 1.26.0
BuildRequires:  crate(tokio-retry-0.3/default) >= 0.3.0
BuildRequires:  crate(tokio-stream-0.1/default) >= 0.1.14
BuildRequires:  crate(toml-1/default) >= 1.0.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.0
BuildRequires:  crate(tracing-log-0.2/default) >= 0.2.0
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.19
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.19
BuildRequires:  crate(url-2/default) >= 2.4.0
BuildRequires:  crate(wait-timeout-0.2/default) >= 0.2.0
BuildRequires:  crate(windows-registry-0.6/default) >= 0.6.0
BuildRequires:  crate(windows-result-0.4/default) >= 0.4.0
BuildRequires:  crate(windows-sys-0.61/default) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-foundation) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-security) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-console) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-diagnostics-toolhelp) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-io) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-ioctl) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-jobobjects) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-kernel) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-libraryloader) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-systeminformation) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-systemservices) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-threading) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-system-windowsprogramming) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-ui) >= 0.61.0
BuildRequires:  crate(windows-sys-0.61/win32-ui-windowsandmessaging) >= 0.61.0
BuildRequires:  crate(xz2-0.1/default) >= 0.1.3
BuildRequires:  crate(zstd-0.13) >= 0.13.0
# Features: curl-backend
BuildRequires:  crate(curl-0.4/default) >= 0.4.44
# Features: reqwest-native-tls
BuildRequires:  crate(env-proxy-0.4/default) >= 0.4.1
BuildRequires:  crate(reqwest-0.13/blocking) >= 0.13.0
BuildRequires:  crate(reqwest-0.13/gzip) >= 0.13.0
BuildRequires:  crate(reqwest-0.13/http2) >= 0.13.0
BuildRequires:  crate(reqwest-0.13/native-tls) >= 0.13.0
BuildRequires:  crate(reqwest-0.13/socks) >= 0.13.0
BuildRequires:  crate(reqwest-0.13/stream) >= 0.13.0
# Features: reqwest-rustls-tls
BuildRequires:  crate(reqwest-0.13/rustls-no-provider) >= 0.13.0
BuildRequires:  crate(rustls-0.23/aws-lc-rs) >= 0.23.0
BuildRequires:  crate(rustls-0.23/logging) >= 0.23.0
BuildRequires:  crate(rustls-0.23/tls12) >= 0.23.0
BuildRequires:  crate(rustls-platform-verifier-0.6/default) >= 0.6.0
# Features: openssl
BuildRequires:  pkgconfig(openssl)
BuildRequires:  crate(openssl-sys-0.9/default) >= 0.9
BuildRequires:  crate(openssl-src-300/default) >= 300.5.4
# Features: test
BuildRequires:  crate(clap-cargo-0.18/testing-colors) >= 0.18.3
BuildRequires:  crate(snapbox-1/default) >= 1.0.0
BuildRequires:  crate(snapbox-1/term-svg) >= 1.0.0
BuildRequires:  crate(walkdir-2/default) >= 2.0.0
# Dev dependencies
BuildRequires:  crate(proptest-1/default) >= 1.1.0
BuildRequires:  crate(httpdate-1/default) >= 1.0.3
BuildRequires:  crate(jni-sys-0.4/default) >= 0.4.1

# Guys we can't install both
Conflicts:      cargo
Conflicts:      rust

%patchlist
# We already on the fixed openssl version...
2000-Remove-pinned-openssl-src-version.patch
2001-Delete-opentelemetry.patch
2002-Remove-pinned-tracing-subscriber-version.patch
# Use the actual build target triple in tests
2003-Fix-RVA23-host-triple-detection-in-rustup-test.patch

%description
Rustup installs The Rust Programming Language from the official release channels,
enabling you to easily switch between stable, beta, and nightly compilers and keep
them updated. It makes cross-compiling simpler with binary builds of the standard
library for common platforms. And it runs on all platforms Rust supports.

%install
install -Dpm 0755 target/release/rustup-init %{buildroot}%{_bindir}/rustup-init
# generate and install shell completions
cp -pav target/release/rustup-init rustup
./rustup completions bash > rustup.bash
./rustup completions fish > rustup.fish
./rustup completions zsh > _rustup

install -Dpm 0644 rustup.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 rustup.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _rustup -t %{buildroot}/%{zsh_completions_dir}

# I have to write my own because otherwise the command will be:
#    cargo test --offline -- --features ...
# and it's not right.
%check
# skip tests that require internet access
# skip tests for the "rustup" binary that is not built in this package
# skip harmless test failures due to mismatch with the "platforms" crate
# skip tests because we change the dependency versions of some crates
cargo test --offline --features test -- \
    --skip suite::cli_exact::check_updates \
    --skip suite::cli_ui::rustup_ui_doc_text_tests \
    --skip suite::known_tuples::gen_known_tuples \
    --skip suite::static_roots::store_static_roots \
    --skip suite::cli_rustup_init_ui::rustup_init_unknown_arg

%files
%doc CHANGELOG.md README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/rustup-init
%{bash_completions_dir}/rustup.bash
%{fish_completions_dir}/rustup.fish
%{zsh_completions_dir}/_rustup

%changelog
%autochangelog
