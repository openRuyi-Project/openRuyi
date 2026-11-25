# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name s3s
%global full_version 0.17.0
%global pkgname s3s-0.17

Name:           rust-s3s-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "s3s"
License:        Apache-2.0
URL:            https://github.com/Nugine/s3s
#!RemoteAsset:  sha256:030a43692a1fd97bbd2c594eeaad8f5c1e452a9d29ad6a3eebce1650937c4a77
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arc-swap-1/default) >= 1.9.2
Requires:       crate(arrayvec-0.7/default) >= 0.7.8
Requires:       crate(async-trait-0.1/default) >= 0.1.92
Requires:       crate(atoi-3) >= 3.1.0
Requires:       crate(base64-simd-0.8/default) >= 0.8.0
Requires:       crate(bytes-1/default) >= 1.12.1
Requires:       crate(bytestring-1/default) >= 1.5.1
Requires:       crate(cfg-if-1/default) >= 1.0.4
Requires:       crate(chrono-0.4) >= 0.4.45
Requires:       crate(crc-fast-1/default) >= 1.10.0
Requires:       crate(futures-0.3/std) >= 0.3.32
Requires:       crate(hex-simd-0.8/default) >= 0.8.0
Requires:       crate(hmac-0.13/default) >= 0.13.0
Requires:       crate(http-1/default) >= 1.4.2
Requires:       crate(http-body-1/default) >= 1.1.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.4
Requires:       crate(hyper-1/default) >= 1.10.1
Requires:       crate(hyper-1/http1) >= 1.10.1
Requires:       crate(hyper-1/http2) >= 1.10.1
Requires:       crate(hyper-1/server) >= 1.10.1
Requires:       crate(itoa-1/default) >= 1.0.18
Requires:       crate(jiff-0.2/default) >= 0.2.35
Requires:       crate(md-5-0.11/default) >= 0.11.0
Requires:       crate(memchr-2/default) >= 2.8.3
Requires:       crate(mime-0.3/default) >= 0.3.17
Requires:       crate(nom-8/default) >= 8.0.0
Requires:       crate(numeric-cast-0.3/default) >= 0.3.0
Requires:       crate(phf-0.14/default) >= 0.14.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(quick-xml-0.42/default) >= 0.42.0
Requires:       crate(quick-xml-0.42/serialize) >= 0.42.0
Requires:       crate(regex-1/default) >= 1.13.1
Requires:       crate(s3s-multipart-0.17/default) >= 0.17.0
Requires:       crate(s3s-rfc2047-0.17/default) >= 0.17.0
Requires:       crate(s3s-sigv2-0.17/default) >= 0.17.0
Requires:       crate(s3s-sigv4-0.17/default) >= 0.17.0
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.150
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.1
Requires:       crate(sha1-0.11/default) >= 0.11.0
Requires:       crate(sha2-0.11/default) >= 0.11.0
Requires:       crate(smallvec-1/default) >= 1.15.2
Requires:       crate(std-next-0.1/default) >= 0.1.9
Requires:       crate(subtle-2/default) >= 2.6.1
Requires:       crate(sync-wrapper-1) >= 1.0.2
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(time-0.3/default) >= 0.3.53
Requires:       crate(time-0.3/formatting) >= 0.3.53
Requires:       crate(time-0.3/macros) >= 0.3.53
Requires:       crate(time-0.3/parsing) >= 0.3.53
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/time) >= 1.52.3
Requires:       crate(tower-0.5) >= 0.5.3
Requires:       crate(tracing-0.1/default) >= 0.1.44
Requires:       crate(transform-stream-0.3/default) >= 0.3.1
Requires:       crate(url-2/default) >= 2.5.8
Requires:       crate(urlencoding-2/default) >= 2.1.3
Requires:       crate(xxhash-rust-0.8/std) >= 0.8.17
Requires:       crate(xxhash-rust-0.8/xxh3) >= 0.8.17
Requires:       crate(xxhash-rust-0.8/xxh64) >= 0.8.17
Requires:       crate(zeroize-1/default) >= 1.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/minio) = %{version}

%description
Source code for takopackized Rust crate "s3s"

%package     -n %{name}+openssl
Summary:        S3 Service Adapter - feature "openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-0.10/default) >= 0.10.81
Requires:       crate(s3s-sigv4-0.17/openssl) >= 0.17.0
Provides:       crate(%{pkgname}/openssl) = %{version}

%description -n %{name}+openssl
This metapackage enables feature "openssl" for the Rust s3s crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
