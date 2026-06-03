# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quinn
%global full_version 0.11.9
%global pkgname quinn-0.11

Name:           rust-quinn-0.11
Version:        0.11.9
Release:        %autorelease
Summary:        Rust crate "quinn"
License:        MIT OR Apache-2.0
URL:            https://github.com/quinn-rs/quinn
#!RemoteAsset:  sha256:b9e20a958963c291dc322d98411f541009df2ced7b5a4f2bd52337638cfccf20
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1.0/default) >= 1.11.0
Requires:       crate(cfg-aliases-0.2/default) >= 0.2.1
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.16
Requires:       crate(quinn-proto-0.11) >= 0.11.13
Requires:       crate(quinn-udp-0.5/tracing) >= 0.5.14
Requires:       crate(rustc-hash-2.0/default) >= 2.1.1
Requires:       crate(socket2-0.6/default) >= 0.6.1
Requires:       crate(thiserror-2.0/default) >= 2.0.17
Requires:       crate(tokio-1.0/default) >= 1.49.0
Requires:       crate(tokio-1.0/sync) >= 1.49.0
Requires:       crate(tracing-0.1/std) >= 0.1.44
Requires:       crate(web-time-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/lock-tracking)

%description
Source code for takopackized Rust crate "quinn"

%package     -n %{name}+aws-lc-rs
Summary:        Versatile QUIC transport protocol implementation - feature "aws-lc-rs"
Requires:       crate(%{pkgname})
Requires:       crate(quinn-proto-0.11/aws-lc-rs) >= 0.11.13
Provides:       crate(%{pkgname}/aws-lc-rs)

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        Versatile QUIC transport protocol implementation - feature "futures-io"
Requires:       crate(%{pkgname})
Requires:       crate(futures-io-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/futures-io)

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Versatile QUIC transport protocol implementation - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(quinn-proto-0.11/log) >= 0.11.13
Requires:       crate(quinn-udp-0.5/log) >= 0.5.14
Requires:       crate(quinn-udp-0.5/tracing) >= 0.5.14
Requires:       crate(tracing-0.1/log) >= 0.1.44
Requires:       crate(tracing-0.1/std) >= 0.1.44
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Versatile QUIC transport protocol implementation - feature "ring"
Requires:       crate(%{pkgname})
Requires:       crate(quinn-proto-0.11/ring) >= 0.11.13
Provides:       crate(%{pkgname}/ring)

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio
Summary:        Versatile QUIC transport protocol implementation - feature "runtime-tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/net) >= 1.49.0
Requires:       crate(tokio-1.0/rt) >= 1.49.0
Requires:       crate(tokio-1.0/sync) >= 1.49.0
Requires:       crate(tokio-1.0/time) >= 1.49.0
Provides:       crate(%{pkgname}/runtime-tokio)

%description -n %{name}+runtime-tokio
This metapackage enables feature "runtime-tokio" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-aws-lc-rs
Summary:        Versatile QUIC transport protocol implementation - feature "rustls-aws-lc-rs"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aws-lc-rs)
Requires:       crate(quinn-proto-0.11/aws-lc-rs) >= 0.11.13
Requires:       crate(quinn-proto-0.11/rustls-aws-lc-rs) >= 0.11.13
Requires:       crate(rustls-0.23/std) >= 0.23.36
Provides:       crate(%{pkgname}/rustls-aws-lc-rs)

%description -n %{name}+rustls-aws-lc-rs
This metapackage enables feature "rustls-aws-lc-rs" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-log
Summary:        Versatile QUIC transport protocol implementation - feature "rustls-log"
Requires:       crate(%{pkgname})
Requires:       crate(rustls-0.23/logging) >= 0.23.36
Requires:       crate(rustls-0.23/std) >= 0.23.36
Provides:       crate(%{pkgname}/rustls-log)

%description -n %{name}+rustls-log
This metapackage enables feature "rustls-log" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-ring
Summary:        Versatile QUIC transport protocol implementation - feature "rustls-ring" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/ring)
Requires:       crate(quinn-proto-0.11/ring) >= 0.11.13
Requires:       crate(quinn-proto-0.11/rustls-ring) >= 0.11.13
Requires:       crate(rustls-0.23/std) >= 0.23.36
Provides:       crate(%{pkgname}/rustls)
Provides:       crate(%{pkgname}/rustls-ring)

%description -n %{name}+rustls-ring
This metapackage enables feature "rustls-ring" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
