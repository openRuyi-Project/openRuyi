# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tower-http
%global full_version 0.5.2
%global pkgname tower-http-0.5

Name:           rust-tower-http-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "tower-http"
License:        MIT
URL:            https://github.com/tower-rs/tower-http
#!RemoteAsset:  sha256:1e9cd434a998747dd2c4276bc96ee2e0c7a2eadf3cae88e52be55a05fa9053f5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.2
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(http-body-1/default) >= 1.0.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.7
Requires:       crate(tower-layer-0.3/default) >= 0.3.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/add-extension) = %{version}
Provides:       crate(%{pkgname}/cors) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/limit) = %{version}
Provides:       crate(%{pkgname}/map-request-body) = %{version}
Provides:       crate(%{pkgname}/map-response-body) = %{version}
Provides:       crate(%{pkgname}/normalize-path) = %{version}
Provides:       crate(%{pkgname}/propagate-header) = %{version}
Provides:       crate(%{pkgname}/redirect) = %{version}
Provides:       crate(%{pkgname}/sensitive-headers) = %{version}
Provides:       crate(%{pkgname}/set-header) = %{version}
Provides:       crate(%{pkgname}/set-status) = %{version}

%description
Source code for takopackized Rust crate "tower-http"

%package     -n %{name}+async-compression
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "async-compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/default) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Provides:       crate(%{pkgname}/async-compression) = %{version}

%description -n %{name}+async-compression
This metapackage enables feature "async-compression" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+auth
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "auth"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/validate-request) = %{version}
Provides:       crate(%{pkgname}/auth) = %{version}

%description -n %{name}+auth
This metapackage enables feature "auth" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+catch-panic
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "catch-panic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(futures-util-0.3/std) >= 0.3.14
Provides:       crate(%{pkgname}/catch-panic) = %{version}

%description -n %{name}+catch-panic
This metapackage enables feature "catch-panic" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-br
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-br" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(async-compression-0.4/brotli) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Provides:       crate(%{pkgname}/compression-br) = %{version}
Provides:       crate(%{pkgname}/decompression-br) = %{version}

%description -n %{name}+compression-br
This metapackage enables feature "compression-br" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "decompression-br" feature.

%package     -n %{name}+compression-deflate
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-deflate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(async-compression-0.4/zlib) >= 0.4.0
Provides:       crate(%{pkgname}/compression-deflate) = %{version}
Provides:       crate(%{pkgname}/decompression-deflate) = %{version}

%description -n %{name}+compression-deflate
This metapackage enables feature "compression-deflate" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "decompression-deflate" feature.

%package     -n %{name}+compression-full
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compression-br) = %{version}
Requires:       crate(%{pkgname}/compression-deflate) = %{version}
Requires:       crate(%{pkgname}/compression-gzip) = %{version}
Requires:       crate(%{pkgname}/compression-zstd) = %{version}
Provides:       crate(%{pkgname}/compression-full) = %{version}

%description -n %{name}+compression-full
This metapackage enables feature "compression-full" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-gzip
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-gzip" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(async-compression-0.4/gzip) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Provides:       crate(%{pkgname}/compression-gzip) = %{version}
Provides:       crate(%{pkgname}/decompression-gzip) = %{version}

%description -n %{name}+compression-gzip
This metapackage enables feature "compression-gzip" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "decompression-gzip" feature.

%package     -n %{name}+compression-zstd
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-zstd" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(async-compression-0.4/zstd) >= 0.4.0
Provides:       crate(%{pkgname}/compression-zstd) = %{version}
Provides:       crate(%{pkgname}/decompression-zstd) = %{version}

%description -n %{name}+compression-zstd
This metapackage enables feature "compression-zstd" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "decompression-zstd" feature.

%package     -n %{name}+decompression-full
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "decompression-full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/decompression-br) = %{version}
Requires:       crate(%{pkgname}/decompression-deflate) = %{version}
Requires:       crate(%{pkgname}/decompression-gzip) = %{version}
Requires:       crate(%{pkgname}/decompression-zstd) = %{version}
Provides:       crate(%{pkgname}/decompression-full) = %{version}

%description -n %{name}+decompression-full
This metapackage enables feature "decompression-full" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+follow-redirect
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "follow-redirect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Requires:       crate(%{pkgname}/iri-string) = %{version}
Requires:       crate(tower-0.4/util) >= 0.4.1
Provides:       crate(%{pkgname}/follow-redirect) = %{version}

%description -n %{name}+follow-redirect
This metapackage enables feature "follow-redirect" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fs
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "fs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Requires:       crate(%{pkgname}/httpdate) = %{version}
Requires:       crate(%{pkgname}/mime) = %{version}
Requires:       crate(%{pkgname}/mime-guess) = %{version}
Requires:       crate(%{pkgname}/percent-encoding) = %{version}
Requires:       crate(%{pkgname}/set-status) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(futures-util-0.3/alloc) >= 0.3.14
Requires:       crate(http-range-header-0.4/default) >= 0.4.0
Requires:       crate(tokio-1/fs) >= 1.6.0
Requires:       crate(tokio-1/io-util) >= 1.6.0
Requires:       crate(tokio-util-0.7/io) >= 0.7.0
Provides:       crate(%{pkgname}/fs) = %{version}

%description -n %{name}+fs
This metapackage enables feature "fs" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/add-extension) = %{version}
Requires:       crate(%{pkgname}/auth) = %{version}
Requires:       crate(%{pkgname}/catch-panic) = %{version}
Requires:       crate(%{pkgname}/compression-full) = %{version}
Requires:       crate(%{pkgname}/cors) = %{version}
Requires:       crate(%{pkgname}/decompression-full) = %{version}
Requires:       crate(%{pkgname}/follow-redirect) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/limit) = %{version}
Requires:       crate(%{pkgname}/map-request-body) = %{version}
Requires:       crate(%{pkgname}/map-response-body) = %{version}
Requires:       crate(%{pkgname}/metrics) = %{version}
Requires:       crate(%{pkgname}/normalize-path) = %{version}
Requires:       crate(%{pkgname}/propagate-header) = %{version}
Requires:       crate(%{pkgname}/redirect) = %{version}
Requires:       crate(%{pkgname}/request-id) = %{version}
Requires:       crate(%{pkgname}/sensitive-headers) = %{version}
Requires:       crate(%{pkgname}/set-header) = %{version}
Requires:       crate(%{pkgname}/set-status) = %{version}
Requires:       crate(%{pkgname}/timeout) = %{version}
Requires:       crate(%{pkgname}/trace) = %{version}
Requires:       crate(%{pkgname}/util) = %{version}
Requires:       crate(%{pkgname}/validate-request) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-util
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "futures-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3) >= 0.3.14
Provides:       crate(%{pkgname}/futures-util) = %{version}

%description -n %{name}+futures-util
This metapackage enables feature "futures-util" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+httpdate
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "httpdate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(httpdate-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/httpdate) = %{version}

%description -n %{name}+httpdate
This metapackage enables feature "httpdate" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+iri-string
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "iri-string"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(iri-string-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/iri-string) = %{version}

%description -n %{name}+iri-string
This metapackage enables feature "iri-string" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+metrics
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "metrics" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/time) >= 1.6.0
Provides:       crate(%{pkgname}/metrics) = %{version}
Provides:       crate(%{pkgname}/timeout) = %{version}

%description -n %{name}+metrics
This metapackage enables feature "metrics" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "timeout" feature.

%package     -n %{name}+mime
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "mime" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mime-0.3) >= 0.3.17
Provides:       crate(%{pkgname}/mime) = %{version}
Provides:       crate(%{pkgname}/validate-request) = %{version}

%description -n %{name}+mime
This metapackage enables feature "mime" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "validate-request" feature.

%package     -n %{name}+mime-guess
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "mime_guess"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mime-guess-2) >= 2.0.0
Provides:       crate(%{pkgname}/mime-guess) = %{version}

%description -n %{name}+mime-guess
This metapackage enables feature "mime_guess" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+percent-encoding
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "percent-encoding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(percent-encoding-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/percent-encoding) = %{version}

%description -n %{name}+percent-encoding
This metapackage enables feature "percent-encoding" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1) >= 1.6.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7/io) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tower
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "tower" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/tower) = %{version}
Provides:       crate(%{pkgname}/util) = %{version}

%description -n %{name}+tower
This metapackage enables feature "tower" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "util" feature.

%package     -n %{name}+tracing
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "tracing" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/trace) = %{version}
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "trace" feature.

%package     -n %{name}+uuid
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "uuid" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.0.0
Requires:       crate(uuid-1/v4) >= 1.0.0
Provides:       crate(%{pkgname}/request-id) = %{version}
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "request-id" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
