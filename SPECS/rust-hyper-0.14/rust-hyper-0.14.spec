# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper
%global full_version 0.14.32
%global pkgname hyper-0.14

Name:           rust-hyper-0.14
Version:        0.14.32
Release:        %autorelease
Summary:        Rust crate "hyper"
License:        MIT
URL:            https://hyper.rs
#!RemoteAsset:  sha256:41dfc780fdec9373c01bae43289ea34c972e40ee3c9f6b3c8801a35f35586ce7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(futures-util-0.3) >= 0.3.0
Requires:       crate(http-0.2/default) >= 0.2.0
Requires:       crate(http-body-0.4/default) >= 0.4.0
Requires:       crate(httparse-1/default) >= 1.8.0
Requires:       crate(httpdate-1/default) >= 1.0.0
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.4
Requires:       crate(tokio-1/default) >= 1.27.0
Requires:       crate(tokio-1/sync) >= 1.27.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Requires:       crate(tracing-0.1/std) >= 0.1.0
Requires:       crate(want-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/backports) = %{version}
Provides:       crate(%{pkgname}/client) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/deprecated) = %{version}
Provides:       crate(%{pkgname}/http1) = %{version}
Provides:       crate(%{pkgname}/internal-happy-eyeballs-tests) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/server) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}

%description
Source code for takopackized Rust crate "hyper"

%package     -n %{name}+full
Summary:        Fast and correct HTTP library - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/client) = %{version}
Requires:       crate(%{pkgname}/http1) = %{version}
Requires:       crate(%{pkgname}/http2) = %{version}
Requires:       crate(%{pkgname}/runtime) = %{version}
Requires:       crate(%{pkgname}/server) = %{version}
Requires:       crate(%{pkgname}/stream) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h2
Summary:        Fast and correct HTTP library - feature "h2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h2-0.3/default) >= 0.3.24
Provides:       crate(%{pkgname}/h2) = %{version}
Provides:       crate(%{pkgname}/http2) = %{version}

%description -n %{name}+h2
This metapackage enables feature "h2" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "http2" feature.

%package     -n %{name}+libc
Summary:        Fast and correct HTTP library - feature "libc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/ffi) = %{version}
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ffi" feature.

%package     -n %{name}+runtime
Summary:        Fast and correct HTTP library - feature "runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tcp) = %{version}
Requires:       crate(tokio-1/rt) >= 1.27.0
Requires:       crate(tokio-1/sync) >= 1.27.0
Requires:       crate(tokio-1/time) >= 1.27.0
Provides:       crate(%{pkgname}/runtime) = %{version}

%description -n %{name}+runtime
This metapackage enables feature "runtime" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socket2
Summary:        Fast and correct HTTP library - feature "socket2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socket2-0.4/all) >= 0.4.7
Requires:       crate(socket2-0.4/default) >= 0.4.7
Provides:       crate(%{pkgname}/socket2) = %{version}

%description -n %{name}+socket2
This metapackage enables feature "socket2" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tcp
Summary:        Fast and correct HTTP library - feature "tcp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/socket2) = %{version}
Requires:       crate(tokio-1/net) >= 1.27.0
Requires:       crate(tokio-1/rt) >= 1.27.0
Requires:       crate(tokio-1/sync) >= 1.27.0
Requires:       crate(tokio-1/time) >= 1.27.0
Provides:       crate(%{pkgname}/tcp) = %{version}

%description -n %{name}+tcp
This metapackage enables feature "tcp" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
