# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git-internal
%global full_version 0.10.4
%global pkgname git-internal-0.10

Name:           rust-git-internal-0.10
Version:        0.10.4
Release:        %autorelease
Summary:        Rust crate "git-internal"
License:        MIT
URL:            https://libra.tools
#!RemoteAsset:  sha256:e56cb086640057dbcb71f0524e3f6412e72d1fd850a985be2151037147d0a939
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/default) >= 0.8.12
Requires:       crate(async-trait-0.1/default) >= 0.1.92
Requires:       crate(axum-0.8/default) >= 0.8.9
Requires:       crate(axum-0.8/json) >= 0.8.9
Requires:       crate(axum-0.8/macros) >= 0.8.9
Requires:       crate(blake3-1/default) >= 1.8.0
Requires:       crate(bstr-1/default) >= 1.13.1
Requires:       crate(byteorder-1/default) >= 1.5.0
Requires:       crate(bytes-1/default) >= 1.12.1
Requires:       crate(chrono-0.4/default) >= 0.4.45
Requires:       crate(chrono-0.4/serde) >= 0.4.45
Requires:       crate(colored-3/default) >= 3.1.1
Requires:       crate(crc32fast-1/default) >= 1.5.0
Requires:       crate(dashmap-6/default) >= 6.2.1
Requires:       crate(diffs-0.5/default) >= 0.5.1
Requires:       crate(encoding-rs-0.8/default) >= 0.8.35
Requires:       crate(flate2-1/zlib-rs) >= 1.1.9
Requires:       crate(futures-0.3/default) >= 0.3.33
Requires:       crate(futures-util-0.3/default) >= 0.3.33
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(libc-0.2/default) >= 0.2.189
Requires:       crate(lru-mem-0.3/default) >= 0.3.0
Requires:       crate(memchr-2/default) >= 2.8.3
Requires:       crate(num-cpus-1/default) >= 1.17.0
Requires:       crate(path-absolutize-4/default) >= 4.0.1
Requires:       crate(rayon-1/default) >= 1.12.0
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.18
Requires:       crate(rkyv-0.8/default) >= 0.8.18
Requires:       crate(serde-1/default) >= 1.0.229
Requires:       crate(serde-1/derive) >= 1.0.229
Requires:       crate(serde-json-1/default) >= 1.0.151
Requires:       crate(sha1-0.11/default) >= 0.11.0
Requires:       crate(sha2-0.11/default) >= 0.11.0
Requires:       crate(similar-3/default) >= 3.1.2
Requires:       crate(tempfile-3/default) >= 3.27.0
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(threadpool-1/default) >= 1.8.1
Requires:       crate(tokio-1/default) >= 1.53.1
Requires:       crate(tokio-1/fs) >= 1.53.1
Requires:       crate(tokio-1/io-util) >= 1.53.1
Requires:       crate(tokio-stream-0.1/default) >= 0.1.19
Requires:       crate(tracing-0.1/default) >= 0.1.44
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.23
Requires:       crate(uuid-1/default) >= 1.24.0
Requires:       crate(uuid-1/serde) >= 1.24.0
Requires:       crate(uuid-1/v4) >= 1.24.0
Requires:       crate(uuid-1/v7) >= 1.24.0
Requires:       crate(zstd-sys-2/default) >= 2.0.16
Requires:       crate(zstd-sys-2/experimental) >= 2.0.16

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bucket-precheck) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/delta-stats) = %{version}
Provides:       crate(%{pkgname}/diff-mydrs) = %{version}
Provides:       crate(%{pkgname}/diff-rabin) = %{version}
Provides:       crate(%{pkgname}/extend-indexed) = %{version}
Provides:       crate(%{pkgname}/extend-ptr) = %{version}
Provides:       crate(%{pkgname}/extend-sliced-index) = %{version}
Provides:       crate(%{pkgname}/extend-sliced-iter) = %{version}
Provides:       crate(%{pkgname}/extend-word) = %{version}

%description
Source code for takopackized Rust crate "git-internal"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
