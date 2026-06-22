# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xet-data
%global full_version 1.5.2
%global pkgname xet-data-1

Name:           rust-xet-data-1
Version:        1.5.2
Release:        %autorelease
Summary:        Rust crate "xet-data"
License:        Apache-2.0
URL:            https://github.com/huggingface/xet-core
#!RemoteAsset:  sha256:67fd409bef621411a9d9013798540bb8036cb2678f03ab39af89a5e88034ed8c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(bytes-1/default) >= 1.11.0
Requires:       crate(chrono-0.4/default) >= 0.4.0
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(gearhash-0.1/default) >= 0.1.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(more-asserts-0.3/default) >= 0.3.0
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(sha2-0.10/asm) >= 0.10.0
Requires:       crate(sha2-0.10/default) >= 0.10.0
Requires:       crate(tempfile-3/default) >= 3.25.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.49.0
Requires:       crate(tokio-1/io-util) >= 1.49.0
Requires:       crate(tokio-1/macros) >= 1.49.0
Requires:       crate(tokio-1/rt) >= 1.49.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.49.0
Requires:       crate(tokio-1/sync) >= 1.49.0
Requires:       crate(tokio-1/time) >= 1.49.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Requires:       crate(url-2/default) >= 2.5.0
Requires:       crate(uuid-1/default) >= 1.0.0
Requires:       crate(uuid-1/v7) >= 1.0.0
Requires:       crate(walkdir-2/default) >= 2.0.0
Requires:       crate(xet-client-1/default) >= 1.5.2
Requires:       crate(xet-core-structures-1/default) >= 1.5.2
Requires:       crate(xet-runtime-1/default) >= 1.5.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/expensive-tests) = %{version}
Provides:       crate(%{pkgname}/smoke-test) = %{version}
Provides:       crate(%{pkgname}/strict) = %{version}

%description
Intended to be used through the API in the hf-xet package.
Source code for takopackized Rust crate "xet-data"

%package     -n %{name}+fd-track
Summary:        Data processing pipeline for chunking, deduplication, and file reconstruction; used in the Hugging Face Xet client tools - feature "fd-track"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xet-client-1/fd-track) >= 1.5.2
Requires:       crate(xet-runtime-1/fd-track) >= 1.5.2
Provides:       crate(%{pkgname}/fd-track) = %{version}

%description -n %{name}+fd-track
Intended to be used through the API in the hf-xet package.
This metapackage enables feature "fd-track" for the Rust xet-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+python
Summary:        Data processing pipeline for chunking, deduplication, and file reconstruction; used in the Hugging Face Xet client tools - feature "python"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-0.26/abi3-py37) >= 0.26.0
Requires:       crate(pyo3-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/python) = %{version}

%description -n %{name}+python
Intended to be used through the API in the hf-xet package.
This metapackage enables feature "python" for the Rust xet-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simulation
Summary:        Data processing pipeline for chunking, deduplication, and file reconstruction; used in the Hugging Face Xet client tools - feature "simulation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xet-client-1/simulation) >= 1.5.2
Requires:       crate(xet-core-structures-1/simulation) >= 1.5.2
Provides:       crate(%{pkgname}/simulation) = %{version}

%description -n %{name}+simulation
Intended to be used through the API in the hf-xet package.
This metapackage enables feature "simulation" for the Rust xet-data crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
