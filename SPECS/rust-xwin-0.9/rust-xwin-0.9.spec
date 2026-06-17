# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xwin
%global full_version 0.9.0
%global pkgname xwin-0.9

Name:           rust-xwin-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "xwin"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Jake-Shadle/xwin
#!RemoteAsset:  sha256:c337699251ad0c38cf87ee63944de38c2201d017cfbb768e5a3897ae835aacc7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(bytes-1/default) >= 1.10.0
Requires:       crate(cab-0.6/default) >= 0.6.0
Requires:       crate(camino-1/default) >= 1.0.0
Requires:       crate(clap-4/default) >= 4.5.0
Requires:       crate(clap-4/derive) >= 4.5.0
Requires:       crate(clap-4/env) >= 4.5.0
Requires:       crate(clap-4/wrap-help) >= 4.5.0
Requires:       crate(cli-table-0.5) >= 0.5.0
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0
Requires:       crate(indicatif-0.18/default) >= 0.18.0
Requires:       crate(memchr-2/default) >= 2.6.0
Requires:       crate(mimalloc-0.1) >= 0.1.0
Requires:       crate(msi-0.10/default) >= 0.10.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(rayon-1/default) >= 1.5.0
Requires:       crate(regex-1/default) >= 1.11.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(sha2-0.11/default) >= 0.11.0
Requires:       crate(tempfile-3/default) >= 3.19.0
Requires:       crate(toml-1/default) >= 1.1.0
Requires:       crate(tracing-0.1/attributes) >= 0.1.0
Requires:       crate(tracing-0.1/std) >= 0.1.0
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/json) >= 0.3.0
Requires:       crate(twox-hash-2/xxhash64) >= 2.1.0
Requires:       crate(ureq-3/gzip) >= 3.0.0
Requires:       crate(ureq-3/platform-verifier) >= 3.0.0
Requires:       crate(ureq-3/rustls) >= 3.0.0
Requires:       crate(ureq-3/socks-proxy) >= 3.0.0
Requires:       crate(versions-7/default) >= 7.0.0
Requires:       crate(walkdir-2/default) >= 2.3.0
Requires:       crate(zip-7/deflate-flate2) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "xwin"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
