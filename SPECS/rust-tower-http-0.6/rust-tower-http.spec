# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tower-http
%global full_version 0.6.8
%global pkgname tower-http-0.6

Name:           rust-tower-http-0.6
Version:        0.6.8
Release:        %autorelease
Summary:        Rust crate "tower-http"
License:        MIT
URL:            https://github.com/tower-rs/tower-http
#!RemoteAsset:  sha256:d4e6559d53cc268e5031cd8429d05415bc4cb4aefc4aa5d6cc35fbf5b924a1f8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(bytes-1.0/default) >= 1.11.1
Requires:       crate(http-1.0/default) >= 1.4.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(tower-layer-0.3/default) >= 0.3.3
Requires:       crate(tower-service-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/add-extension)
Provides:       crate(%{pkgname}/cors)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/map-request-body)
Provides:       crate(%{pkgname}/map-response-body)
Provides:       crate(%{pkgname}/normalize-path)
Provides:       crate(%{pkgname}/propagate-header)
Provides:       crate(%{pkgname}/redirect)
Provides:       crate(%{pkgname}/sensitive-headers)
Provides:       crate(%{pkgname}/set-header)
Provides:       crate(%{pkgname}/set-status)

%description
Source code for takopackized Rust crate "tower-http"

%package     -n %{name}+async-compression
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "async-compression"
Requires:       crate(%{pkgname})
Requires:       crate(async-compression-0.4/default) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Provides:       crate(%{pkgname}/async-compression)

%description -n %{name}+async-compression
This metapackage enables feature "async-compression" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+auth
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "auth"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/base64)
Requires:       crate(%{pkgname}/validate-request)
Provides:       crate(%{pkgname}/auth)

%description -n %{name}+auth
This metapackage enables feature "auth" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "base64"
Requires:       crate(%{pkgname})
Requires:       crate(base64-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/base64)

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+catch-panic
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "catch-panic"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(futures-util-0.3/std) >= 0.3.32
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/catch-panic)

%description -n %{name}+catch-panic
This metapackage enables feature "catch-panic" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-br
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-br"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(async-compression-0.4/brotli) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname}/compression-br)

%description -n %{name}+compression-br
This metapackage enables feature "compression-br" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-deflate
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-deflate"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(async-compression-0.4/zlib) >= 0.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname}/compression-deflate)

%description -n %{name}+compression-deflate
This metapackage enables feature "compression-deflate" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-full
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compression-br)
Requires:       crate(%{pkgname}/compression-deflate)
Requires:       crate(%{pkgname}/compression-gzip)
Requires:       crate(%{pkgname}/compression-zstd)
Provides:       crate(%{pkgname}/compression-full)

%description -n %{name}+compression-full
This metapackage enables feature "compression-full" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-gzip
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-gzip"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(async-compression-0.4/gzip) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname}/compression-gzip)

%description -n %{name}+compression-gzip
This metapackage enables feature "compression-gzip" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-zstd
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "compression-zstd"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(async-compression-0.4/zstd) >= 0.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname}/compression-zstd)

%description -n %{name}+compression-zstd
This metapackage enables feature "compression-zstd" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+decompression-br
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "decompression-br"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(async-compression-0.4/brotli) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/decompression-br)

%description -n %{name}+decompression-br
This metapackage enables feature "decompression-br" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+decompression-deflate
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "decompression-deflate"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(async-compression-0.4/zlib) >= 0.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/decompression-deflate)

%description -n %{name}+decompression-deflate
This metapackage enables feature "decompression-deflate" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+decompression-full
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "decompression-full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/decompression-br)
Requires:       crate(%{pkgname}/decompression-deflate)
Requires:       crate(%{pkgname}/decompression-gzip)
Requires:       crate(%{pkgname}/decompression-zstd)
Provides:       crate(%{pkgname}/decompression-full)

%description -n %{name}+decompression-full
This metapackage enables feature "decompression-full" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+decompression-gzip
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "decompression-gzip"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(async-compression-0.4/gzip) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/decompression-gzip)

%description -n %{name}+decompression-gzip
This metapackage enables feature "decompression-gzip" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+decompression-zstd
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "decompression-zstd"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(async-compression-0.4/zstd) >= 0.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/decompression-zstd)

%description -n %{name}+decompression-zstd
This metapackage enables feature "decompression-zstd" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+follow-redirect
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "follow-redirect"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-util)
Requires:       crate(%{pkgname}/iri-string)
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(tower-0.5/util) >= 0.5.3
Provides:       crate(%{pkgname}/follow-redirect)

%description -n %{name}+follow-redirect
This metapackage enables feature "follow-redirect" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fs
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "fs"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/futures-util)
Requires:       crate(%{pkgname}/httpdate)
Requires:       crate(%{pkgname}/mime)
Requires:       crate(%{pkgname}/mime-guess)
Requires:       crate(%{pkgname}/percent-encoding)
Requires:       crate(%{pkgname}/set-status)
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(futures-util-0.3/alloc) >= 0.3.32
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Requires:       crate(http-range-header-0.4/default) >= 0.4.0
Requires:       crate(tokio-1.0/fs) >= 1.6
Requires:       crate(tokio-1.0/io-util) >= 1.6
Requires:       crate(tokio-util-0.7/io) >= 0.7.0
Provides:       crate(%{pkgname}/fs)

%description -n %{name}+fs
This metapackage enables feature "fs" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/add-extension)
Requires:       crate(%{pkgname}/auth)
Requires:       crate(%{pkgname}/catch-panic)
Requires:       crate(%{pkgname}/compression-full)
Requires:       crate(%{pkgname}/cors)
Requires:       crate(%{pkgname}/decompression-full)
Requires:       crate(%{pkgname}/follow-redirect)
Requires:       crate(%{pkgname}/fs)
Requires:       crate(%{pkgname}/limit)
Requires:       crate(%{pkgname}/map-request-body)
Requires:       crate(%{pkgname}/map-response-body)
Requires:       crate(%{pkgname}/metrics)
Requires:       crate(%{pkgname}/normalize-path)
Requires:       crate(%{pkgname}/propagate-header)
Requires:       crate(%{pkgname}/redirect)
Requires:       crate(%{pkgname}/request-id)
Requires:       crate(%{pkgname}/sensitive-headers)
Requires:       crate(%{pkgname}/set-header)
Requires:       crate(%{pkgname}/set-status)
Requires:       crate(%{pkgname}/timeout)
Requires:       crate(%{pkgname}/trace)
Requires:       crate(%{pkgname}/util)
Requires:       crate(%{pkgname}/validate-request)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "futures-core"
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures-core)

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-util
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "futures-util"
Requires:       crate(%{pkgname})
Requires:       crate(futures-util-0.3) >= 0.3.32
Provides:       crate(%{pkgname}/futures-util)

%description -n %{name}+futures-util
This metapackage enables feature "futures-util" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+httpdate
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "httpdate"
Requires:       crate(%{pkgname})
Requires:       crate(httpdate-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/httpdate)

%description -n %{name}+httpdate
This metapackage enables feature "httpdate" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+iri-string
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "iri-string"
Requires:       crate(%{pkgname})
Requires:       crate(iri-string-0.7/default) >= 0.7.12
Provides:       crate(%{pkgname}/iri-string)

%description -n %{name}+iri-string
This metapackage enables feature "iri-string" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+limit
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "limit"
Requires:       crate(%{pkgname})
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/limit)

%description -n %{name}+limit
This metapackage enables feature "limit" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+metrics
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "metrics" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(tokio-1.0/time) >= 1.6
Provides:       crate(%{pkgname}/metrics)
Provides:       crate(%{pkgname}/timeout)

%description -n %{name}+metrics
This metapackage enables feature "metrics" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "timeout" feature.

%package     -n %{name}+mime
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "mime" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(mime-0.3) >= 0.3.17
Provides:       crate(%{pkgname}/mime)
Provides:       crate(%{pkgname}/validate-request)

%description -n %{name}+mime
This metapackage enables feature "mime" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "validate-request" feature.

%package     -n %{name}+mime-guess
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "mime_guess"
Requires:       crate(%{pkgname})
Requires:       crate(mime-guess-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/mime-guess)

%description -n %{name}+mime-guess
This metapackage enables feature "mime_guess" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+percent-encoding
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "percent-encoding"
Requires:       crate(%{pkgname})
Requires:       crate(percent-encoding-2.0/default) >= 2.1.0
Provides:       crate(%{pkgname}/percent-encoding)

%description -n %{name}+percent-encoding
This metapackage enables feature "percent-encoding" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0) >= 1.6
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "tokio-util"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-util-0.7/io) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util)

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tower
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "tower" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(tower-0.5/default) >= 0.5.3
Provides:       crate(%{pkgname}/tower)
Provides:       crate(%{pkgname}/util)

%description -n %{name}+tower
This metapackage enables feature "tower" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "util" feature.

%package     -n %{name}+trace
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "trace"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(http-body-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname}/trace)

%description -n %{name}+trace
This metapackage enables feature "trace" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Tower middleware and utilities for HTTP clients and servers - feature "uuid" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(uuid-1.0/default) >= 1.0.0
Requires:       crate(uuid-1.0/v4) >= 1.0.0
Provides:       crate(%{pkgname}/request-id)
Provides:       crate(%{pkgname}/uuid)

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust tower-http crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "request-id" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
