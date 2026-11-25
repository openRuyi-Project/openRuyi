# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libfuse-fs
%global full_version 0.1.13
%global pkgname libfuse-fs-0.1

Name:           rust-libfuse-fs-0.1
Version:        0.1.13
Release:        %autorelease
Summary:        Rust crate "libfuse-fs"
License:        MIT OR Apache-2.0
URL:            https://github.com/r2cn-dev/rk8s/tree/main/project/libfuse-fs
#!RemoteAsset:  sha256:d61be2a0235d6a5ba30064c172f12d5465da0f013281a0e6675604d0781496e9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.89
Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(bitflags-2/serde) >= 2.4.0
Requires:       crate(bytes-1/default) >= 1.10.1
Requires:       crate(clap-4/default) >= 4.5.49
Requires:       crate(clap-4/derive) >= 4.5.49
Requires:       crate(futures-0.3/default) >= 0.3.31
Requires:       crate(futures-util-0.3/default) >= 0.3.31
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(libc-0.2/default) >= 0.2.175
Requires:       crate(lru-0.16/default) >= 0.16.0
Requires:       crate(memmap2-0.9/default) >= 0.9.7
Requires:       crate(moka-0.12/default) >= 0.12.11
Requires:       crate(moka-0.12/future) >= 0.12.11
Requires:       crate(nix-0.29/default) >= 0.29.0
Requires:       crate(radix-trie-0.2/default) >= 0.2.1
Requires:       crate(reqwest-0.12/blocking) >= 0.12.24
Requires:       crate(reqwest-0.12/default) >= 0.12.24
Requires:       crate(reqwest-0.12/json) >= 0.12.24
Requires:       crate(rfuse3-0.0.8/default) >= 0.0.8
Requires:       crate(rfuse3-0.0.8/file-lock) >= 0.0.8
Requires:       crate(rfuse3-0.0.8/tokio-runtime) >= 0.0.8
Requires:       crate(rfuse3-0.0.8/unprivileged) >= 0.0.8
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.145
Requires:       crate(tokio-1/default) >= 1.48.0
Requires:       crate(tokio-1/full) >= 1.48.0
Requires:       crate(tracing-0.1/default) >= 0.1.41
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.20
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.20
Requires:       crate(tracing-subscriber-0.3/json) >= 0.3.20
Requires:       crate(uuid-1/default) >= 1.18.1
Requires:       crate(uuid-1/fast-rng) >= 1.18.1
Requires:       crate(uuid-1/macro-diagnostics) >= 1.18.1
Requires:       crate(uuid-1/serde) >= 1.18.1
Requires:       crate(uuid-1/v4) >= 1.18.1
Requires:       crate(vm-memory-0.16/default) >= 0.16.1
Requires:       crate(vmm-sys-util-0.12/default) >= 0.12.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libfuse-fs"

%prep -a
# The crates.io archive includes a precompiled x86-64 test fixture.
rm tests/ior

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
