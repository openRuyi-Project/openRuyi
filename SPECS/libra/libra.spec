# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libra
Version:        0.30.329
Release:        %autorelease
Summary:        Command-line version control client
License:        MIT
URL:            https://github.com/libra-tools/libra
VCS:            git:https://github.com/libra-tools/libra.git
#!RemoteAsset:  sha256:f8e97d8edcbe3a3d4b9c1fb3b5f92ac8bcf6b1d31f6f230edfe0f3a2f61c2e20
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/libra-v%{version}.tar.gz
# Keep desktop features optional for the command-line package.
Patch2000:      2000-make-desktop-optional.patch
# Use dependencies available from the distribution's Cargo registry.
Patch2001:      2001-use-system-deps-for-cli.patch
# Build the packaged CLI with SQLite and without the desktop application.
Patch2002:      2002-limit-rpm-to-sqlite-cli-features.patch
# Run the packaged Git import and content checks.
Patch2003:      2003-use-cli-smoke-test-in-rpm.patch
# Enable Deflate in the selected ZIP crate.
Patch2004:      2004-enable-zip-deflate.patch
BuildSystem:    rust

BuildOption(build):  --bin libra --no-default-features --features storage-sqlite

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  unzip
BuildRequires:  pkgconfig(openssl)
BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(async-stream-0.3/default) >= 0.3.6
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.89
BuildRequires:  crate(axum-0.8/default) >= 0.8.9
BuildRequires:  crate(base64-0.22/default) >= 0.22.1
BuildRequires:  crate(byte-unit-5/default) >= 5.2.0
BuildRequires:  crate(byteorder-1/default) >= 1.5.0
BuildRequires:  crate(bytes-1/default) >= 1.11.1
BuildRequires:  crate(bzip2-0.6/default) >= 0.6
BuildRequires:  crate(chrono-0.4/default) >= 0.4.44
BuildRequires:  crate(chrono-0.4/serde) >= 0.4.44
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(clap-complete-4/default) >= 4.6.6
BuildRequires:  crate(colored-3/default) >= 3.1.1
BuildRequires:  crate(crc32fast-1/default) >= 1.5.0
BuildRequires:  crate(diffs-0.5/default) >= 0.5.1
BuildRequires:  crate(diffy-0.4/default) >= 0.4.2
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(errno-0.3/default) >= 0.3
BuildRequires:  crate(fancy-regex-0.16/default) >= 0.16.2
BuildRequires:  crate(fastrand-2/default) >= 2.3.0
BuildRequires:  crate(flate2-1/default) >= 1.1.9
BuildRequires:  crate(futures-0.3/default) >= 0.3.32
BuildRequires:  crate(futures-core-0.3/default) >= 0.3.32
BuildRequires:  crate(futures-util-0.3/default) >= 0.3.32
BuildRequires:  crate(git-internal-0.10/default) = 0.10.4
BuildRequires:  crate(hex-0.4/default) >= 0.4.3
BuildRequires:  crate(http-1/default) >= 1.4.0
BuildRequires:  crate(ignore-0.4/default) >= 0.4.25
BuildRequires:  crate(indicatif-0.18/default) >= 0.18.4
BuildRequires:  crate(lazy-static-1/default) >= 1.5.0
BuildRequires:  crate(libc-0.2/default) >= 0.2
BuildRequires:  crate(libfuse-fs-0.1/default) >= 0.1.13
BuildRequires:  crate(libvault-0.4/default) >= 0.4.0
BuildRequires:  crate(libvault-0.4/storage-sqlite) >= 0.4.0
BuildRequires:  crate(lru-mem-0.3/default) >= 0.3.0
BuildRequires:  crate(object-store-0.13/aws) >= 0.13.2
BuildRequires:  crate(object-store-0.13/azure) >= 0.13.2
BuildRequires:  crate(object-store-0.13/default) >= 0.13.2
BuildRequires:  crate(object-store-0.13/gcp) >= 0.13.2
BuildRequires:  crate(object-store-0.13/http) >= 0.13.2
BuildRequires:  crate(once-cell-1/default) >= 1.21.4
BuildRequires:  crate(openssl-0.10/default) >= 0.10.78
BuildRequires:  crate(path-absolutize-3/default) >= 3.1.1
BuildRequires:  crate(pathdiff-0.2/default) >= 0.2.3
BuildRequires:  crate(pgp-0.19/default) >= 0.19.0
BuildRequires:  crate(pulldown-cmark-0.13/default) >= 0.13.3
BuildRequires:  crate(rand-0.8/default) >= 0.8.5
BuildRequires:  crate(regex-1/default) >= 1.12.3
BuildRequires:  crate(reqwest-0.13/json) >= 0.13.2
BuildRequires:  crate(reqwest-0.13/query) >= 0.13.2
BuildRequires:  crate(reqwest-0.13/rustls) >= 0.13.2
BuildRequires:  crate(reqwest-0.13/stream) >= 0.13.2
BuildRequires:  crate(rfuse3-0.0.8/default) >= 0.0.8
BuildRequires:  crate(rfuse3-0.0.8/tokio-runtime) >= 0.0.8
BuildRequires:  crate(rfuse3-0.0.8/unprivileged) >= 0.0.8
BuildRequires:  crate(ring-0.17/default) >= 0.17.14
BuildRequires:  crate(rpassword-7/default) >= 7.4.0
BuildRequires:  crate(rsa-0.9/default) >= 0.9
BuildRequires:  crate(sea-orm-2/default) >= 2.0.0
BuildRequires:  crate(sea-orm-2/macros) >= 2.0.0
BuildRequires:  crate(sea-orm-2/runtime-tokio-rustls) >= 2.0.0
BuildRequires:  crate(sea-orm-2/sqlx-sqlite) >= 2.0.0
# Cargo resolves the optional SeaORM Arrow source when writing the lockfile.
BuildRequires:  crate(sea-orm-arrow-2.0.0-rc.3) = 2.0.0
BuildRequires:  crate(seccompiler-0.5/default) >= 0.5.0
BuildRequires:  crate(seccompiler-0.5/json) >= 0.5.0
BuildRequires:  crate(semver-1/default) >= 1.0.27
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.149
BuildRequires:  crate(serde-json-1/raw-value) >= 1.0.149
BuildRequires:  crate(sha1-0.11/default) >= 0.11.0
BuildRequires:  crate(sha2-0.10/default) >= 0.10
BuildRequires:  crate(shlex-1/default) >= 1.3.0
BuildRequires:  crate(similar-3/default) >= 3.1.1
BuildRequires:  crate(syntect-5/default-syntaxes) >= 5.3.0
BuildRequires:  crate(syntect-5/regex-fancy) >= 5.3.0
BuildRequires:  crate(tar-0.4/default) >= 0.4
BuildRequires:  crate(tempfile-3/default) >= 3.27.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.18
BuildRequires:  crate(tokio-1/default) >= 1.52.1
BuildRequires:  crate(tokio-1/io-std) >= 1.52.1
BuildRequires:  crate(tokio-1/io-util) >= 1.52.1
BuildRequires:  crate(tokio-1/macros) >= 1.52.1
BuildRequires:  crate(tokio-1/net) >= 1.52.1
BuildRequires:  crate(tokio-1/process) >= 1.52.1
BuildRequires:  crate(tokio-1/rt) >= 1.52.1
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.52.1
BuildRequires:  crate(tokio-1/signal) >= 1.52.1
BuildRequires:  crate(tokio-1/sync) >= 1.52.1
BuildRequires:  crate(tokio-1/time) >= 1.52.1
BuildRequires:  crate(tokio-stream-0.1/default) >= 0.1.18
BuildRequires:  crate(tokio-stream-0.1/sync) >= 0.1.18
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.18
BuildRequires:  crate(tokio-util-0.7/io) >= 0.7.18
BuildRequires:  crate(toml-0.8/default) >= 0.8.23
BuildRequires:  crate(tracing-0.1/default) >= 0.1.44
BuildRequires:  crate(tracing-appender-0.2/default) >= 0.2.3
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.23
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.23
BuildRequires:  crate(tree-sitter-0.26/default) >= 0.26.8
BuildRequires:  crate(tree-sitter-bash-0.25/default) >= 0.25
BuildRequires:  crate(unicode-normalization-0.1/default) = 0.1.25
BuildRequires:  crate(unicode-width-0.2/default) >= 0.2.2
BuildRequires:  crate(url-2/default) >= 2.5.8
BuildRequires:  crate(uuid-1/default) >= 1.23.1
BuildRequires:  crate(uuid-1/v4) >= 1.23.1
BuildRequires:  crate(uuid-1/v5) >= 1.23.1
BuildRequires:  crate(uuid-1/v7) >= 1.23.1
BuildRequires:  crate(walkdir-2/default) >= 2.5.0
BuildRequires:  crate(wax-0.7/default) >= 0.7.0
BuildRequires:  crate(zeroize-1/default) >= 1
BuildRequires:  crate(zip-0.6/default) >= 0.6
BuildRequires:  crate(zip-0.6/deflate) >= 0.6

%description
Libra is a version-control client supporting Git objects and repositories.
This package builds the command-line client with SQLite storage.

%build -p
export OPENSSL_NO_VENDOR=1
export RUST_LOCK_POLICY=ignore

%install
install -Dpm0755 target/release/libra %{buildroot}%{_bindir}/libra

%check
libra="$PWD/target/release/libra"
"$libra" --version | grep -Fx "libra %{version}"
testdir=$(mktemp -d)
git init -b main "$testdir/git"
printf 'openRuyi packaging check\n' > "$testdir/git/payload"
git -C "$testdir/git" add payload
git -C "$testdir/git" -c user.name=RPM -c user.email=packaging@example.invalid commit -m "Verify Git import"
git -C "$testdir/git" gc
expected=$(git -C "$testdir/git" rev-parse HEAD)
mkdir "$testdir/libra"
(
  cd "$testdir/libra"
  "$libra" init --vault false --from-git-repository "$testdir/git"
  test "$("$libra" rev-parse HEAD)" = "$expected"
  test "$("$libra" show --offline HEAD:payload)" = "openRuyi packaging check"
  "$libra" archive --offline --format zip --output "$testdir/check.zip" HEAD
  test "$(unzip -p "$testdir/check.zip" payload)" = "openRuyi packaging check"
)

%files
%doc README.md
%license LICENSE
%{_bindir}/libra

%changelog
%autochangelog
