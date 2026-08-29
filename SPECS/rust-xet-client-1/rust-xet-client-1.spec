# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xet-client
%global full_version 1.5.2
%global pkgname xet-client-1

Name:           rust-xet-client-1
Version:        1.5.2
Release:        %autorelease
Summary:        Rust crate "xet-client"
License:        Apache-2.0
URL:            https://github.com/huggingface/xet-core
#!RemoteAsset:  sha256:3e1e496dcbe6a09017acdfaf48e1a646735e7ff5b2a49e2c7e081cca77a59bc8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(bytes-1/default) >= 1.11.0
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(crc32fast-1/default) >= 1.5.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(hyper-1/default) >= 1.8.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(more-asserts-0.3/default) >= 0.3.0
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(redb-3/default) >= 3.1.0
Requires:       crate(reqwest-0.13/json) >= 0.13.1
Requires:       crate(reqwest-0.13/socks) >= 0.13.1
Requires:       crate(reqwest-0.13/stream) >= 0.13.1
Requires:       crate(reqwest-0.13/system-proxy) >= 0.13.1
Requires:       crate(reqwest-middleware-0.5/default) >= 0.5.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(serde-repr-0.1/default) >= 0.1.0
Requires:       crate(statrs-0.18) >= 0.18.0
Requires:       crate(tempfile-3/default) >= 3.25.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.49.0
Requires:       crate(tokio-1/io-util) >= 1.49.0
Requires:       crate(tokio-1/macros) >= 1.49.0
Requires:       crate(tokio-1/rt) >= 1.49.0
Requires:       crate(tokio-1/sync) >= 1.49.0
Requires:       crate(tokio-1/time) >= 1.49.0
Requires:       crate(tokio-retry-0.3/default) >= 0.3.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/json) >= 0.3.0
Requires:       crate(url-2/default) >= 2.5.0
Requires:       crate(urlencoding-2/default) >= 2.1.0
Requires:       crate(web-time-1/default) >= 1.1.0
Requires:       crate(xet-core-structures-1/default) >= 1.5.2
Requires:       crate(xet-runtime-1/default) >= 1.5.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/analysis) = %{version}
Provides:       crate(%{pkgname}/elevated-information-level) = %{version}
Provides:       crate(%{pkgname}/smoke-test) = %{version}
Provides:       crate(%{pkgname}/strict) = %{version}

%description
Use through the hf-xet crate.
Source code for takopackized Rust crate "xet-client"

%package     -n %{name}+fd-track
Summary:        Client library for communicating with Hugging Face Xet storage servers - feature "fd-track"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xet-runtime-1/fd-track) >= 1.5.2
Provides:       crate(%{pkgname}/fd-track) = %{version}

%description -n %{name}+fd-track
Use through the hf-xet crate.
This metapackage enables feature "fd-track" for the Rust xet-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Client library for communicating with Hugging Face Xet storage servers - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/json) >= 0.13.1
Requires:       crate(reqwest-0.13/native-tls) >= 0.13.1
Requires:       crate(reqwest-0.13/socks) >= 0.13.1
Requires:       crate(reqwest-0.13/stream) >= 0.13.1
Requires:       crate(reqwest-0.13/system-proxy) >= 0.13.1
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
Use through the hf-xet crate.
This metapackage enables feature "native-tls" for the Rust xet-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-vendored
Summary:        Client library for communicating with Hugging Face Xet storage servers - feature "native-tls-vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/json) >= 0.13.1
Requires:       crate(reqwest-0.13/native-tls-vendored) >= 0.13.1
Requires:       crate(reqwest-0.13/socks) >= 0.13.1
Requires:       crate(reqwest-0.13/stream) >= 0.13.1
Requires:       crate(reqwest-0.13/system-proxy) >= 0.13.1
Provides:       crate(%{pkgname}/native-tls-vendored) = %{version}

%description -n %{name}+native-tls-vendored
Use through the hf-xet crate.
This metapackage enables feature "native-tls-vendored" for the Rust xet-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls
Summary:        Client library for communicating with Hugging Face Xet storage servers - feature "rustls-tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/json) >= 0.13.1
Requires:       crate(reqwest-0.13/rustls) >= 0.13.1
Requires:       crate(reqwest-0.13/socks) >= 0.13.1
Requires:       crate(reqwest-0.13/stream) >= 0.13.1
Requires:       crate(reqwest-0.13/system-proxy) >= 0.13.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustls-tls) = %{version}

%description -n %{name}+rustls-tls
Use through the hf-xet crate.
This metapackage enables feature "rustls-tls" for the Rust xet-client crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+simulation
Summary:        Client library for communicating with Hugging Face Xet storage servers - feature "simulation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(axum-0.8/default) >= 0.8.0
Requires:       crate(futures-util-0.3/default) >= 0.3.0
Requires:       crate(human-bandwidth-0.1/default) >= 0.1.0
Requires:       crate(humantime-2/default) >= 2.1.0
Requires:       crate(tower-http-0.6/cors) >= 0.6.0
Requires:       crate(tower-http-0.6/default) >= 0.6.0
Requires:       crate(xet-core-structures-1/simulation) >= 1.5.2
Provides:       crate(%{pkgname}/simulation) = %{version}

%description -n %{name}+simulation
Use through the hf-xet crate.
This metapackage enables feature "simulation" for the Rust xet-client crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
