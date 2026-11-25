# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qrustls
%global full_version 0.23.45
%global pkgname qrustls-0.23

Name:           rust-qrustls-0.23
Version:        0.23.45
Release:        %autorelease
Summary:        Rust crate "qrustls"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/genmeta/rustls
#!RemoteAsset:  sha256:8050bd9948ac6868ddadcb6bf58e5da7a46ad922acd595db4a9ba04578139c2f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/alloc) >= 1.16.0
Requires:       crate(once-cell-1/race) >= 1.16.0
Requires:       crate(rustls-pki-types-1/alloc) >= 1.12.0
Requires:       crate(rustls-pki-types-1/default) >= 1.12.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.14
Requires:       crate(subtle-2) >= 2.5.0
Requires:       crate(zeroize-1/default) >= 1.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/custom-provider) = %{version}
Provides:       crate(%{pkgname}/tls12) = %{version}

%description
Source code for takopackized Rust crate "qrustls"

%package     -n %{name}+aws-lc-rs
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "aws_lc_rs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-rs-1) >= 1.18.0
Requires:       crate(aws-lc-rs-1/aws-lc-sys) >= 1.18.0
Requires:       crate(aws-lc-rs-1/prebuilt-nasm) >= 1.18.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.14
Requires:       crate(rustls-webpki-0.103/aws-lc-rs) >= 0.103.14
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}
Provides:       crate(%{pkgname}/prefer-post-quantum) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws_lc_rs" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "prefer-post-quantum" feature.

%package     -n %{name}+brotli
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(brotli-8/std) >= 8.0.0
Requires:       crate(brotli-decompressor-5/default) >= 5.0.0
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/prefer-post-quantum) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tls12) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(aws-lc-rs-1/fips) >= 1.18.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.14
Requires:       crate(rustls-webpki-0.103/aws-lc-rs-fips) >= 0.103.14
Provides:       crate(%{pkgname}/fips) = %{version}

%description -n %{name}+fips
This metapackage enables feature "fips" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.0
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "logging" feature.

%package     -n %{name}+read-buf
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "read_buf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustversion) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/read-buf) = %{version}

%description -n %{name}+read-buf
This metapackage enables feature "read_buf" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.14
Requires:       crate(rustls-webpki-0.103/ring) >= 0.103.14
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustversion
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "rustversion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustversion-1/default) >= 1.0.6
Provides:       crate(%{pkgname}/rustversion) = %{version}

%description -n %{name}+rustversion
This metapackage enables feature "rustversion" for the Rust qrustls crate,
by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/alloc) >= 1.16.0
Requires:       crate(once-cell-1/race) >= 1.16.0
Requires:       crate(once-cell-1/std) >= 1.16.0
Requires:       crate(rustls-pki-types-1/alloc) >= 1.12.0
Requires:       crate(rustls-pki-types-1/std) >= 1.12.0
Requires:       crate(rustls-webpki-0.103/alloc) >= 0.103.14
Requires:       crate(rustls-webpki-0.103/std) >= 0.103.14
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib
Summary:        Rustls fork for QUIC with client OCSP stapling and protected session persistence - feature "zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zlib-rs-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/zlib) = %{version}

%description -n %{name}+zlib
This metapackage enables feature "zlib" for the Rust qrustls crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
