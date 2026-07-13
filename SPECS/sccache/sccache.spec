# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sccache

Name:           sccache
Version:        0.16.0
Release:        %autorelease
Summary:        ccache-like compiler caching tool
License:        Apache-2.0
URL:            https://github.com/mozilla/sccache
#!RemoteAsset:  sha256:d4462c4a5371468689d3e13b4f1eef708e547010cdf19613debe25a7799a6c53
Source:         https://static.crates.io/crates/%{crate_name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

# Drop the cloud/dist backends and dev deps, keep local disk caching only.
Patch2000:      2000-strip-unused-deps.patch

BuildOption(build):  -- --bin sccache

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anyhow-1/backtrace) >= 1.0.102
BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(ar-0.9/default) >= 0.9.0
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.89
BuildRequires:  crate(backon-1/std-blocking-sleep) >= 1.6.0
BuildRequires:  crate(base64-0.21/default) >= 0.21.7
BuildRequires:  crate(bincode-1/default) >= 1.3.3
BuildRequires:  crate(blake3-1/default) >= 1.8.4
BuildRequires:  crate(byteorder-1/default) >= 1.5.0
BuildRequires:  crate(bytes-1/default) >= 1.11.1
BuildRequires:  crate(chrono-0.4/default) >= 0.4.44
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(clap-4/env) >= 4.6.1
BuildRequires:  crate(clap-4/wrap-help) >= 4.6.1
BuildRequires:  crate(daemonix-0.1/default) >= 0.1.0
BuildRequires:  crate(directories-6/default) >= 6.0.0
BuildRequires:  crate(encoding-rs-0.8/default) >= 0.8.35
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.10
BuildRequires:  crate(filetime-0.2/default) >= 0.2.27
BuildRequires:  crate(fs-err-3/default) >= 3.3.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.32
BuildRequires:  crate(gzp-2/deflate-rust) >= 2.0.2
BuildRequires:  crate(http-1/default) >= 1.4.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(jobserver-0.1/default) >= 0.1.34
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(linked-hash-map-0.5/default) >= 0.5.6
BuildRequires:  crate(log-0.4/default) >= 0.4.30
BuildRequires:  crate(memchr-2/default) >= 2.8.1
BuildRequires:  crate(memmap2-0.9/default) >= 0.9.10
BuildRequires:  crate(mime-0.3/default) >= 0.3.17
BuildRequires:  crate(number-prefix-0.4/default) >= 0.4.0
BuildRequires:  crate(object-0.37/default) >= 0.37.3
BuildRequires:  crate(rand-0.8/default) >= 0.8.6
BuildRequires:  crate(regex-1/default) >= 1.12.3
BuildRequires:  crate(semver-1/default) >= 1.0.28
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(shlex-1/default) >= 1.3.0
BuildRequires:  crate(strip-ansi-escapes-0.2/default) >= 0.2.1
BuildRequires:  crate(tar-0.4/default) >= 0.4.46
BuildRequires:  crate(tempfile-3/default) >= 3.27.0
BuildRequires:  crate(tokio-1/default) >= 1.52.3
BuildRequires:  crate(tokio-1/io-util) >= 1.52.3
BuildRequires:  crate(tokio-1/macros) >= 1.52.3
BuildRequires:  crate(tokio-1/net) >= 1.52.3
BuildRequires:  crate(tokio-1/process) >= 1.52.3
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.52.3
BuildRequires:  crate(tokio-1/time) >= 1.52.3
BuildRequires:  crate(tokio-serde-0.9/default) >= 0.9.0
BuildRequires:  crate(tokio-util-0.7/codec) >= 0.7.18
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.18
BuildRequires:  crate(tokio-util-0.7/io) >= 0.7.18
BuildRequires:  crate(toml-0.9/default) >= 0.9.12
BuildRequires:  crate(tower-service-0.3/default) >= 0.3.3
BuildRequires:  crate(typed-path-0.12/default) >= 0.12.3
BuildRequires:  crate(uuid-1/default) >= 1.23.2
BuildRequires:  crate(uuid-1/v4) >= 1.23.2
BuildRequires:  crate(walkdir-2/default) >= 2.5.0
BuildRequires:  crate(which-6) >= 6.0.3
BuildRequires:  crate(windows-sys-0.52/default) >= 0.52.0
BuildRequires:  crate(windows-sys-0.52/win32-foundation) >= 0.52.0
BuildRequires:  crate(windows-sys-0.52/win32-globalization) >= 0.52.0
BuildRequires:  crate(windows-sys-0.52/win32-security) >= 0.52.0
BuildRequires:  crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0
BuildRequires:  crate(windows-sys-0.52/win32-system-console) >= 0.52.0
BuildRequires:  crate(windows-sys-0.52/win32-system-threading) >= 0.52.0
BuildRequires:  crate(zip-0.6) >= 0.6.6
BuildRequires:  crate(zstd-0.13/default) >= 0.13.3

%description
Sccache is a ccache-like compiler caching tool. It is used as a compiler
wrapper and avoids compilation when possible, storing cached results in
local disk storage (or, in the full-featured build, in remote/cloud
storage). This package builds the client with local disk caching only.

%build -p
%ifarch riscv64
export RUST_MIN_STACK=16777216
export CARGO_PROFILE_RELEASE_LTO=false
export CARGO_PROFILE_RELEASE_OPT_LEVEL=2
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16
%endif

%install
install -Dm0755 target/release/sccache %{buildroot}%{_bindir}/sccache

%check
# The patch drops the dev-dependencies, so the tests cannot be built.

%files
%doc README.md
%license LICENSE
%{_bindir}/sccache

%changelog
%autochangelog
