# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls
%global full_version 0.23.37
%global pkgname rustls-0.23

Name:           rust-rustls-0.23
Version:        0.23.37
Release:        %autorelease
Summary:        Rust crate "rustls"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/rustls/rustls
#!RemoteAsset:  sha256:758025cb5fccfd3bc2fd74708fd4682be41d99e5dff73c377c0646c6012c73a4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/alloc) >= 1.16.0
Requires:       crate(once-cell-1/race) >= 1.16.0
Requires:       crate(rustls-pki-types-1/alloc) >= 1.12.0
Requires:       crate(rustls-pki-types-1/default) >= 1.12.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.5
Requires:       crate(subtle-2) >= 2.5.0
Requires:       crate(zeroize-1/default) >= 1.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/custom-provider) = %{version}
Provides:       crate(%{pkgname}/tls12) = %{version}

%description
Source code for takopackized Rust crate "rustls"

%package     -n %{name}+aws-lc-rs
Summary:        Modern TLS library written in Rust - feature "aws_lc_rs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-rs-1) >= 1.14.0
Requires:       crate(aws-lc-rs-1/aws-lc-sys) >= 1.14.0
Requires:       crate(aws-lc-rs-1/prebuilt-nasm) >= 1.14.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.5
Requires:       crate(rustls-webpki-0.103/aws-lc-rs) >= 0.103.5
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}
Provides:       crate(%{pkgname}/prefer-post-quantum) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws_lc_rs" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "prefer-post-quantum" feature.

%package     -n %{name}+brotli
Summary:        Modern TLS library written in Rust - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(brotli-8/std) >= 8.0.0
Requires:       crate(brotli-decompressor-5/default) >= 5.0.0
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Modern TLS library written in Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/prefer-post-quantum) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tls12) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Modern TLS library written in Rust - feature "fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(aws-lc-rs-1/fips) >= 1.14.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.5
Requires:       crate(rustls-webpki-0.103/aws-lc-rs-fips) >= 0.103.5
Provides:       crate(%{pkgname}/fips) = %{version}

%description -n %{name}+fips
This metapackage enables feature "fips" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Modern TLS library written in Rust - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.0
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Modern TLS library written in Rust - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "logging" feature.

%package     -n %{name}+read-buf
Summary:        Modern TLS library written in Rust - feature "read_buf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustversion) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/read-buf) = %{version}

%description -n %{name}+read-buf
This metapackage enables feature "read_buf" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Modern TLS library written in Rust - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.5
Requires:       crate(rustls-webpki-0.103/ring) >= 0.103.5
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustversion
Summary:        Modern TLS library written in Rust - feature "rustversion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustversion-1/default) >= 1.0.6
Provides:       crate(%{pkgname}/rustversion) = %{version}

%description -n %{name}+rustversion
This metapackage enables feature "rustversion" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Modern TLS library written in Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/alloc) >= 1.16.0
Requires:       crate(once-cell-1/race) >= 1.16.0
Requires:       crate(once-cell-1/std) >= 1.16.0
Requires:       crate(rustls-pki-types-1/alloc) >= 1.12.0
Requires:       crate(rustls-pki-types-1/std) >= 1.12.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.5
Requires:       crate(rustls-webpki-0.103/std) >= 0.103.5
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib
Summary:        Modern TLS library written in Rust - feature "zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zlib-rs-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/zlib) = %{version}

%description -n %{name}+zlib
This metapackage enables feature "zlib" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
