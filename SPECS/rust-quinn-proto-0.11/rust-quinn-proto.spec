# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
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

Requires:       crate(bytes-1.0/default) >= 1.11.0
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.4
Requires:       crate(lru-slab-0.1/default) >= 0.1.2
Requires:       crate(rand-0.9/default) >= 0.9.2
Requires:       crate(ring-0.17/default) >= 0.17.14
Requires:       crate(ring-0.17/wasm32-unknown-unknown-js) >= 0.17.14
Requires:       crate(rustc-hash-2.0/default) >= 2.1.1
Requires:       crate(rustls-pki-types-1.0/default) >= 1.13.2
Requires:       crate(rustls-pki-types-1.0/web) >= 1.13.2
Requires:       crate(slab-0.4/default) >= 0.4.11
Requires:       crate(thiserror-2.0/default) >= 2.0.17
Requires:       crate(tinyvec-1.0/alloc) >= 1.10.0
Requires:       crate(tinyvec-1.0/default) >= 1.10.0
Requires:       crate(tracing-0.1/std) >= 0.1.44
Requires:       crate(web-time-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "quinn-proto"

%package     -n %{name}+aws-lc-rs
Summary:        State machine for the QUIC transport protocol - feature "aws-lc-rs"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-rs-1.0) >= 1.9
Requires:       crate(aws-lc-rs-1.0/aws-lc-sys) >= 1.9
Requires:       crate(aws-lc-rs-1.0/prebuilt-nasm) >= 1.9
Provides:       crate(%{pkgname}/aws-lc-rs)

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        State machine for the QUIC transport protocol - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1/log) >= 0.1.44
Requires:       crate(tracing-0.1/std) >= 0.1.44
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        State machine for the QUIC transport protocol - feature "ring"
Requires:       crate(%{pkgname})
Requires:       crate(ring-0.17/default) >= 0.17.14
Requires:       crate(ring-0.17/wasm32-unknown-unknown-js) >= 0.17.14
Provides:       crate(%{pkgname}/ring)

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-aws-lc-rs
Summary:        State machine for the QUIC transport protocol - feature "rustls-aws-lc-rs"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aws-lc-rs)
Requires:       crate(rustls-0.23/aws-lc-rs) >= 0.23.36
Requires:       crate(rustls-0.23/std) >= 0.23.36
Provides:       crate(%{pkgname}/rustls-aws-lc-rs)

%description -n %{name}+rustls-aws-lc-rs
This metapackage enables feature "rustls-aws-lc-rs" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-log
Summary:        State machine for the QUIC transport protocol - feature "rustls-log"
Requires:       crate(%{pkgname})
Requires:       crate(rustls-0.23/logging) >= 0.23.36
Requires:       crate(rustls-0.23/std) >= 0.23.36
Provides:       crate(%{pkgname}/rustls-log)

%description -n %{name}+rustls-log
This metapackage enables feature "rustls-log" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-ring
Summary:        State machine for the QUIC transport protocol - feature "rustls-ring" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/ring)
Requires:       crate(rustls-0.23/ring) >= 0.23.36
Requires:       crate(rustls-0.23/std) >= 0.23.36
Provides:       crate(%{pkgname}/rustls)
Provides:       crate(%{pkgname}/rustls-ring)

%description -n %{name}+rustls-ring
This metapackage enables feature "rustls-ring" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
