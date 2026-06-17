# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-compression
%global full_version 0.4.25
%global pkgname async-compression-0.4

Name:           rust-async-compression-0.4
Version:        0.4.25
Release:        %autorelease
Summary:        Rust crate "async-compression"
License:        MIT OR Apache-2.0
URL:            https://github.com/Nullus157/async-compression
#!RemoteAsset:  sha256:40f6024f3f856663b45fd0c9b6f2024034a702f453549449e0d84a305900dad4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(memchr-2/default) >= 2.0.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-compression"

%package     -n %{name}+all
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all-algorithms) = %{version}
Requires:       crate(%{pkgname}/all-implementations) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-algorithms
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "all-algorithms"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/brotli) = %{version}
Requires:       crate(%{pkgname}/bzip2) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/deflate64) = %{version}
Requires:       crate(%{pkgname}/gzip) = %{version}
Requires:       crate(%{pkgname}/lz4) = %{version}
Requires:       crate(%{pkgname}/lzma) = %{version}
Requires:       crate(%{pkgname}/xz) = %{version}
Requires:       crate(%{pkgname}/zlib) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/all-algorithms) = %{version}

%description -n %{name}+all-algorithms
This metapackage enables feature "all-algorithms" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-implementations
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "all-implementations"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-io) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/all-implementations) = %{version}

%description -n %{name}+all-implementations
This metapackage enables feature "all-implementations" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+brotli
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-8/default) >= 8.0.0
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bzip2
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "bzip2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/bzip2) = %{version}

%description -n %{name}+bzip2
This metapackage enables feature "bzip2" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate64
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "deflate64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(deflate64-0.1/default) >= 0.1.5
Provides:       crate(%{pkgname}/deflate64) = %{version}

%description -n %{name}+deflate64
This metapackage enables feature "deflate64" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "flate2" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.13
Provides:       crate(%{pkgname}/deflate) = %{version}
Provides:       crate(%{pkgname}/flate2) = %{version}
Provides:       crate(%{pkgname}/gzip) = %{version}
Provides:       crate(%{pkgname}/zlib) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "deflate", "gzip", and "zlib" features.

%package     -n %{name}+futures-io
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/std) >= 0.3.0
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libzstd
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "libzstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13) >= 0.13.1
Provides:       crate(%{pkgname}/libzstd) = %{version}

%description -n %{name}+libzstd
This metapackage enables feature "libzstd" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lz4
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "lz4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lz4-1/default) >= 1.28.1
Provides:       crate(%{pkgname}/lz4) = %{version}

%description -n %{name}+lz4
This metapackage enables feature "lz4" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lzma
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "lzma" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(liblzma-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/lzma) = %{version}
Provides:       crate(%{pkgname}/xz) = %{version}
Provides:       crate(%{pkgname}/xz2) = %{version}

%description -n %{name}+lzma
This metapackage enables feature "lzma" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "xz", and "xz2" features.

%package     -n %{name}+tokio
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1) >= 1.24.2
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libzstd) = %{version}
Requires:       crate(%{pkgname}/zstd-safe) = %{version}
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd-safe
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "zstd-safe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-safe-7) >= 7.0.0
Provides:       crate(%{pkgname}/zstd-safe) = %{version}

%description -n %{name}+zstd-safe
This metapackage enables feature "zstd-safe" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstdmt
Summary:        Adaptors between compression crates and Rust's modern asynchronous IO types - feature "zstdmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Requires:       crate(zstd-safe-7/zstdmt) >= 7.0.0
Provides:       crate(%{pkgname}/zstdmt) = %{version}

%description -n %{name}+zstdmt
This metapackage enables feature "zstdmt" for the Rust async-compression crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
