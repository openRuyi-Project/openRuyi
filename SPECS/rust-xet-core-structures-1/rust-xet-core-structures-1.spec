# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xet-core-structures
%global full_version 1.5.2
%global pkgname xet-core-structures-1

Name:           rust-xet-core-structures-1
Version:        1.5.2
Release:        %autorelease
Summary:        Rust crate "xet-core-structures"
License:        Apache-2.0
URL:            https://github.com/huggingface/xet-core
#!RemoteAsset:  sha256:cb838aa8eb67d730af301584cf003caad407487606058292a6750711b603fbee
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(blake3-1/default) >= 1.8.0
Requires:       crate(bytemuck-1/default) >= 1.0.0
Requires:       crate(bytes-1/default) >= 1.11.0
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(countio-0.3/default) >= 0.3.0
Requires:       crate(countio-0.3/futures) >= 0.3.0
Requires:       crate(csv-1/default) >= 1.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(futures-util-0.3/default) >= 0.3.0
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(getrandom-0.4/wasm-js) >= 0.4.0
Requires:       crate(heapify-0.2/default) >= 0.2.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(lz4-flex-0.13/default) >= 0.13.0
Requires:       crate(more-asserts-0.3/default) >= 0.3.0
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(safe-transmute-0.11/default) >= 0.11.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(static-assertions-1/default) >= 1.1.0
Requires:       crate(tempfile-3/default) >= 3.25.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.49.0
Requires:       crate(tokio-1/io-util) >= 1.49.0
Requires:       crate(tokio-1/macros) >= 1.49.0
Requires:       crate(tokio-1/rt) >= 1.49.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.49.0
Requires:       crate(tokio-1/sync) >= 1.49.0
Requires:       crate(tokio-1/test-util) >= 1.49.0
Requires:       crate(tokio-1/time) >= 1.49.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.0
Requires:       crate(tokio-util-0.7/io) >= 0.7.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Requires:       crate(uuid-1/default) >= 1.0.0
Requires:       crate(uuid-1/js) >= 1.0.0
Requires:       crate(uuid-1/v4) >= 1.0.0
Requires:       crate(web-time-1/default) >= 1.1.0
Requires:       crate(xet-runtime-1/default) >= 1.5.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/smoke-test) = %{version}
Provides:       crate(%{pkgname}/strict) = %{version}

%description
Source code for takopackized Rust crate "xet-core-structures"

%package     -n %{name}+simulation
Summary:        Core data structures including MerkleHash, metadata shards, and Xorb objects - feature "simulation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xet-runtime-1/simulation) >= 1.5.2
Provides:       crate(%{pkgname}/simulation) = %{version}

%description -n %{name}+simulation
This metapackage enables feature "simulation" for the Rust xet-core-structures crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
