# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quinn-proto
%global full_version 0.11.13
%global pkgname quinn-proto-0.11

Name:           rust-quinn-proto-0.11
Version:        0.11.13
Release:        %autorelease
Summary:        Rust crate "quinn-proto"
License:        MIT OR Apache-2.0
URL:            https://github.com/quinn-rs/quinn
#!RemoteAsset:  sha256:f1906b49b0c3bc04b5fe5d86a77925ae6524a19b816ae38ce1e426255f1d8a31
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.0
Requires:       crate(lru-slab-0.1/default) >= 0.1.2
Requires:       crate(rand-0.9/default) >= 0.9.0
Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(ring-0.17/wasm32-unknown-unknown-js) >= 0.17.0
Requires:       crate(rustc-hash-2/default) >= 2.0.0
Requires:       crate(rustls-pki-types-1/default) >= 1.7.0
Requires:       crate(rustls-pki-types-1/web) >= 1.7.0
Requires:       crate(slab-0.4/default) >= 0.4.6
Requires:       crate(thiserror-2/default) >= 2.0.3
Requires:       crate(tinyvec-1/alloc) >= 1.1.0
Requires:       crate(tinyvec-1/default) >= 1.1.0
Requires:       crate(tracing-0.1/std) >= 0.1.10
Requires:       crate(web-time-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "quinn-proto"

%package     -n %{name}+arbitrary
Summary:        State machine for the QUIC transport protocol - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.1
Requires:       crate(arbitrary-1/derive) >= 1.0.1
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-rs
Summary:        State machine for the QUIC transport protocol - feature "aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-rs-1) >= 1.9.0
Requires:       crate(aws-lc-rs-1/aws-lc-sys) >= 1.9.0
Requires:       crate(aws-lc-rs-1/prebuilt-nasm) >= 1.9.0
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-rs-fips
Summary:        State machine for the QUIC transport protocol - feature "aws-lc-rs-fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(aws-lc-rs-1/fips) >= 1.9.0
Provides:       crate(%{pkgname}/aws-lc-rs-fips) = %{version}

%description -n %{name}+aws-lc-rs-fips
This metapackage enables feature "aws-lc-rs-fips" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bloom
Summary:        State machine for the QUIC transport protocol - feature "bloom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fastbloom-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/bloom) = %{version}

%description -n %{name}+bloom
This metapackage enables feature "bloom" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        State machine for the QUIC transport protocol - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bloom) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/rustls-ring) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        State machine for the QUIC transport protocol - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/log) >= 0.1.10
Requires:       crate(tracing-0.1/std) >= 0.1.10
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+platform-verifier
Summary:        State machine for the QUIC transport protocol - feature "platform-verifier"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-platform-verifier-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/platform-verifier) = %{version}

%description -n %{name}+platform-verifier
This metapackage enables feature "platform-verifier" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+qlog
Summary:        State machine for the QUIC transport protocol - feature "qlog"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(qlog-0.15/default) >= 0.15.2
Provides:       crate(%{pkgname}/qlog) = %{version}

%description -n %{name}+qlog
This metapackage enables feature "qlog" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        State machine for the QUIC transport protocol - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(ring-0.17/wasm32-unknown-unknown-js) >= 0.17.0
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-aws-lc-rs
Summary:        State machine for the QUIC transport protocol - feature "rustls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(rustls-0.23/aws-lc-rs) >= 0.23.5
Requires:       crate(rustls-0.23/std) >= 0.23.5
Provides:       crate(%{pkgname}/rustls-aws-lc-rs) = %{version}

%description -n %{name}+rustls-aws-lc-rs
This metapackage enables feature "rustls-aws-lc-rs" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-aws-lc-rs-fips
Summary:        State machine for the QUIC transport protocol - feature "rustls-aws-lc-rs-fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs-fips) = %{version}
Requires:       crate(%{pkgname}/rustls-aws-lc-rs) = %{version}
Provides:       crate(%{pkgname}/rustls-aws-lc-rs-fips) = %{version}

%description -n %{name}+rustls-aws-lc-rs-fips
This metapackage enables feature "rustls-aws-lc-rs-fips" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-log
Summary:        State machine for the QUIC transport protocol - feature "rustls-log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.5
Requires:       crate(rustls-0.23/std) >= 0.23.5
Provides:       crate(%{pkgname}/rustls-log) = %{version}

%description -n %{name}+rustls-log
This metapackage enables feature "rustls-log" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-ring
Summary:        State machine for the QUIC transport protocol - feature "rustls-ring" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ring) = %{version}
Requires:       crate(rustls-0.23/ring) >= 0.23.5
Requires:       crate(rustls-0.23/std) >= 0.23.5
Provides:       crate(%{pkgname}/rustls) = %{version}
Provides:       crate(%{pkgname}/rustls-ring) = %{version}

%description -n %{name}+rustls-ring
This metapackage enables feature "rustls-ring" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
