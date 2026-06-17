# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-rustls
%global full_version 0.26.4
%global pkgname tokio-rustls-0.26

Name:           rust-tokio-rustls-0.26
Version:        0.26.4
Release:        %autorelease
Summary:        Rust crate "tokio-rustls"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustls/tokio-rustls
#!RemoteAsset:  sha256:1729aa945f29d91ba541258c8df89027d5792d85a8841fb65e8bf0f4ede4ef61
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-0.23/std) >= 0.23.27
Requires:       crate(tokio-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/early-data) = %{version}

%description
Source code for takopackized Rust crate "tokio-rustls"

%package     -n %{name}+aws-lc-rs
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "aws_lc_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/aws-lc-rs) >= 0.23.27
Requires:       crate(rustls-0.23/std) >= 0.23.27
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws_lc_rs" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+brotli
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/brotli) >= 0.23.27
Requires:       crate(rustls-0.23/std) >= 0.23.27
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/tls12) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/fips) >= 0.23.27
Requires:       crate(rustls-0.23/std) >= 0.23.27
Provides:       crate(%{pkgname}/fips) = %{version}

%description -n %{name}+fips
This metapackage enables feature "fips" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.27
Requires:       crate(rustls-0.23/std) >= 0.23.27
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/ring) >= 0.23.27
Requires:       crate(rustls-0.23/std) >= 0.23.27
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls12
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "tls12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/std) >= 0.23.27
Requires:       crate(rustls-0.23/tls12) >= 0.23.27
Provides:       crate(%{pkgname}/tls12) = %{version}

%description -n %{name}+tls12
This metapackage enables feature "tls12" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/std) >= 0.23.27
Requires:       crate(rustls-0.23/zlib) >= 0.23.27
Provides:       crate(%{pkgname}/zlib) = %{version}

%description -n %{name}+zlib
This metapackage enables feature "zlib" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
