# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(cfg-aliases-0.2) >= 0.2.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(quinn-proto-0.11) >= 0.11.12
Requires:       crate(quinn-udp-0.5/tracing) >= 0.5.0
Requires:       crate(rustc-hash-2/default) >= 2.0.0
Requires:       crate(socket2-0.5/default) >= 0.5.0
Requires:       crate(thiserror-2/default) >= 2.0.3
Requires:       crate(tokio-1/default) >= 1.28.1
Requires:       crate(tokio-1/sync) >= 1.28.1
Requires:       crate(tracing-0.1/std) >= 0.1.10
Requires:       crate(web-time-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/lock-tracking) = %{version}

%description
Source code for takopackized Rust crate "quinn"

%package     -n %{name}+async-io
Summary:        Versatile QUIC transport protocol implementation - feature "async-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/async-io) = %{version}

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Versatile QUIC transport protocol implementation - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-rs
Summary:        Versatile QUIC transport protocol implementation - feature "aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.11/aws-lc-rs) >= 0.11.12
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-rs-fips
Summary:        Versatile QUIC transport protocol implementation - feature "aws-lc-rs-fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.11/aws-lc-rs-fips) >= 0.11.12
Provides:       crate(%{pkgname}/aws-lc-rs-fips) = %{version}

%description -n %{name}+aws-lc-rs-fips
This metapackage enables feature "aws-lc-rs-fips" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bloom
Summary:        Versatile QUIC transport protocol implementation - feature "bloom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.11/bloom) >= 0.11.12
Provides:       crate(%{pkgname}/bloom) = %{version}

%description -n %{name}+bloom
This metapackage enables feature "bloom" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Versatile QUIC transport protocol implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bloom) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/platform-verifier) = %{version}
Requires:       crate(%{pkgname}/runtime-tokio) = %{version}
Requires:       crate(%{pkgname}/rustls-ring) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        Versatile QUIC transport protocol implementation - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Versatile QUIC transport protocol implementation - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.11/log) >= 0.11.12
Requires:       crate(quinn-udp-0.5/log) >= 0.5.0
Requires:       crate(quinn-udp-0.5/tracing) >= 0.5.0
Requires:       crate(tracing-0.1/log) >= 0.1.10
Requires:       crate(tracing-0.1/std) >= 0.1.10
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+platform-verifier
Summary:        Versatile QUIC transport protocol implementation - feature "platform-verifier"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.11/platform-verifier) >= 0.11.12
Provides:       crate(%{pkgname}/platform-verifier) = %{version}

%description -n %{name}+platform-verifier
This metapackage enables feature "platform-verifier" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+qlog
Summary:        Versatile QUIC transport protocol implementation - feature "qlog"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.11/qlog) >= 0.11.12
Provides:       crate(%{pkgname}/qlog) = %{version}

%description -n %{name}+qlog
This metapackage enables feature "qlog" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Versatile QUIC transport protocol implementation - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.11/ring) >= 0.11.12
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std
Summary:        Versatile QUIC transport protocol implementation - feature "runtime-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-io) = %{version}
Requires:       crate(%{pkgname}/async-std) = %{version}
Provides:       crate(%{pkgname}/runtime-async-std) = %{version}

%description -n %{name}+runtime-async-std
This metapackage enables feature "runtime-async-std" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-smol
Summary:        Versatile QUIC transport protocol implementation - feature "runtime-smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-io) = %{version}
Requires:       crate(%{pkgname}/smol) = %{version}
Provides:       crate(%{pkgname}/runtime-smol) = %{version}

%description -n %{name}+runtime-smol
This metapackage enables feature "runtime-smol" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio
Summary:        Versatile QUIC transport protocol implementation - feature "runtime-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/net) >= 1.28.1
Requires:       crate(tokio-1/rt) >= 1.28.1
Requires:       crate(tokio-1/sync) >= 1.28.1
Requires:       crate(tokio-1/time) >= 1.28.1
Provides:       crate(%{pkgname}/runtime-tokio) = %{version}

%description -n %{name}+runtime-tokio
This metapackage enables feature "runtime-tokio" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-aws-lc-rs
Summary:        Versatile QUIC transport protocol implementation - feature "rustls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(quinn-proto-0.11/aws-lc-rs) >= 0.11.12
Requires:       crate(quinn-proto-0.11/rustls-aws-lc-rs) >= 0.11.12
Requires:       crate(rustls-0.23/std) >= 0.23.5
Provides:       crate(%{pkgname}/rustls-aws-lc-rs) = %{version}

%description -n %{name}+rustls-aws-lc-rs
This metapackage enables feature "rustls-aws-lc-rs" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-aws-lc-rs-fips
Summary:        Versatile QUIC transport protocol implementation - feature "rustls-aws-lc-rs-fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs-fips) = %{version}
Requires:       crate(quinn-proto-0.11/aws-lc-rs-fips) >= 0.11.12
Requires:       crate(quinn-proto-0.11/rustls-aws-lc-rs-fips) >= 0.11.12
Requires:       crate(rustls-0.23/std) >= 0.23.5
Provides:       crate(%{pkgname}/rustls-aws-lc-rs-fips) = %{version}

%description -n %{name}+rustls-aws-lc-rs-fips
This metapackage enables feature "rustls-aws-lc-rs-fips" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-log
Summary:        Versatile QUIC transport protocol implementation - feature "rustls-log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.5
Requires:       crate(rustls-0.23/std) >= 0.23.5
Provides:       crate(%{pkgname}/rustls-log) = %{version}

%description -n %{name}+rustls-log
This metapackage enables feature "rustls-log" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-ring
Summary:        Versatile QUIC transport protocol implementation - feature "rustls-ring" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ring) = %{version}
Requires:       crate(quinn-proto-0.11/ring) >= 0.11.12
Requires:       crate(quinn-proto-0.11/rustls-ring) >= 0.11.12
Requires:       crate(rustls-0.23/std) >= 0.23.5
Provides:       crate(%{pkgname}/rustls) = %{version}
Provides:       crate(%{pkgname}/rustls-ring) = %{version}

%description -n %{name}+rustls-ring
This metapackage enables feature "rustls-ring" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls" feature.

%package     -n %{name}+smol
Summary:        Versatile QUIC transport protocol implementation - feature "smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smol-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/smol) = %{version}

%description -n %{name}+smol
This metapackage enables feature "smol" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
