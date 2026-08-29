# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name flate2
%global full_version 1.1.9
%global pkgname flate2-1

Name:           rust-flate2-1
Version:        1.1.9
Release:        %autorelease
Summary:        Rust crate "flate2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/flate2-rs
#!RemoteAsset:  sha256:843fba2746e448b37e26a819579957415c8cef339bf08564fe8b7ddbd959573c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(miniz-oxide-0.8/simd) >= 0.8.5
Requires:       crate(miniz-oxide-0.8/with-alloc) >= 0.8.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/any-c-zlib) = %{version}
Provides:       crate(%{pkgname}/any-impl) = %{version}
Provides:       crate(%{pkgname}/any-zlib) = %{version}

%description
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
Source code for takopackized Rust crate "flate2"

%package     -n %{name}+cloudflare-zlib-sys
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "cloudflare-zlib-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cloudflare-zlib-sys-0.3/default) >= 0.3.6
Provides:       crate(%{pkgname}/cloudflare-zlib-sys) = %{version}

%description -n %{name}+cloudflare-zlib-sys
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "cloudflare-zlib-sys" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cloudflare-zlib
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "cloudflare_zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any-c-zlib) = %{version}
Requires:       crate(%{pkgname}/cloudflare-zlib-sys) = %{version}
Requires:       crate(crc32fast-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/cloudflare-zlib) = %{version}

%description -n %{name}+cloudflare-zlib
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "cloudflare_zlib" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "document-features" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libz-ng-sys
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "libz-ng-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libz-ng-sys-1/default) >= 1.1.16
Provides:       crate(%{pkgname}/libz-ng-sys) = %{version}

%description -n %{name}+libz-ng-sys
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "libz-ng-sys" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libz-sys
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "libz-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libz-sys-1) >= 1.1.20
Provides:       crate(%{pkgname}/libz-sys) = %{version}

%description -n %{name}+libz-sys
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "libz-sys" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+miniz-oxide
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "miniz_oxide"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any-impl) = %{version}
Requires:       crate(crc32fast-1/default) >= 1.2.0
Requires:       crate(miniz-oxide-0.8/simd) >= 0.8.5
Requires:       crate(miniz-oxide-0.8/with-alloc) >= 0.8.5
Provides:       crate(%{pkgname}/miniz-oxide) = %{version}

%description -n %{name}+miniz-oxide
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "miniz_oxide" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-backend
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "rust_backend" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any-impl) = %{version}
Requires:       crate(%{pkgname}/miniz-oxide) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/miniz-sys) = %{version}
Provides:       crate(%{pkgname}/rust-backend) = %{version}

%description -n %{name}+rust-backend
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "rust_backend" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "miniz-sys" features.

%package     -n %{name}+zlib
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any-c-zlib) = %{version}
Requires:       crate(%{pkgname}/libz-sys) = %{version}
Requires:       crate(crc32fast-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/zlib) = %{version}

%description -n %{name}+zlib
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "zlib" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-default
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "zlib-default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any-c-zlib) = %{version}
Requires:       crate(crc32fast-1/default) >= 1.2.0
Requires:       crate(libz-sys-1/default) >= 1.1.20
Provides:       crate(%{pkgname}/zlib-default) = %{version}

%description -n %{name}+zlib-default
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "zlib-default" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "zlib-ng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any-c-zlib) = %{version}
Requires:       crate(%{pkgname}/libz-ng-sys) = %{version}
Requires:       crate(crc32fast-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/zlib-ng) = %{version}

%description -n %{name}+zlib-ng
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "zlib-ng" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "zlib-ng-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/zlib) = %{version}
Requires:       crate(crc32fast-1/default) >= 1.2.0
Requires:       crate(libz-sys-1/zlib-ng) >= 1.1.20
Provides:       crate(%{pkgname}/zlib-ng-compat) = %{version}

%description -n %{name}+zlib-ng-compat
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "zlib-ng-compat" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-rs
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams - feature "zlib-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any-zlib) = %{version}
Requires:       crate(zlib-rs-0.6/rust-allocator) >= 0.6.0
Requires:       crate(zlib-rs-0.6/std) >= 0.6.0
Provides:       crate(%{pkgname}/zlib-rs) = %{version}

%description -n %{name}+zlib-rs
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
This metapackage enables feature "zlib-rs" for the Rust flate2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
