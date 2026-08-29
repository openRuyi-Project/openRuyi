# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name console-subscriber
%global full_version 0.5.0
%global pkgname console-subscriber-0.5

Name:           rust-console-subscriber-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "console-subscriber"
License:        MIT
URL:            https://github.com/tokio-rs/console/blob/main/console-subscriber
#!RemoteAsset:  sha256:fb4915b7d8dd960457a1b6c380114c2944f728e7c65294ab247ae6b6f1f37592
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(console-api-0.9/default) >= 0.9.0
Requires:       crate(console-api-0.9/transport) >= 0.9.0
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.7
Requires:       crate(futures-task-0.3) >= 0.3.31
Requires:       crate(hdrhistogram-7/serialization) >= 7.4.0
Requires:       crate(humantime-2/default) >= 2.1.0
Requires:       crate(hyper-util-0.1/default) >= 0.1.6
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.6
Requires:       crate(prost-0.14/default) >= 0.14.1
Requires:       crate(prost-types-0.14/default) >= 0.14.1
Requires:       crate(serde-1/default) >= 1.0.145
Requires:       crate(serde-1/derive) >= 1.0.145
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(thread-local-1/default) >= 1.1.4
Requires:       crate(tokio-1/default) >= 1.47.1
Requires:       crate(tokio-1/macros) >= 1.47.1
Requires:       crate(tokio-1/sync) >= 1.47.1
Requires:       crate(tokio-1/time) >= 1.47.1
Requires:       crate(tokio-1/tracing) >= 1.47.1
Requires:       crate(tokio-stream-0.1/default) >= 0.1.16
Requires:       crate(tokio-stream-0.1/net) >= 0.1.16
Requires:       crate(tonic-0.14/default) >= 0.14.2
Requires:       crate(tonic-0.14/transport) >= 0.14.2
Requires:       crate(tracing-0.1/default) >= 0.1.35
Requires:       crate(tracing-core-0.1/default) >= 0.1.30
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.17
Requires:       crate(tracing-subscriber-0.3/registry) >= 0.3.17
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/grpc-web) = %{version}

%description
Source code for takopackized Rust crate "console-subscriber"

%package     -n %{name}+env-filter
Summary:        `tracing-subscriber::Layer` for collecting Tokio console telemetry - feature "env-filter" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.17
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.17
Requires:       crate(tracing-subscriber-0.3/registry) >= 0.3.17
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/env-filter) = %{version}

%description -n %{name}+env-filter
This metapackage enables feature "env-filter" for the Rust console-subscriber crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+parking-lot
Summary:        `tracing-subscriber::Layer` for collecting Tokio console telemetry - feature "parking_lot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.12/default) >= 0.12.1
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.17
Requires:       crate(tracing-subscriber-0.3/parking-lot) >= 0.3.17
Requires:       crate(tracing-subscriber-0.3/registry) >= 0.3.17
Provides:       crate(%{pkgname}/parking-lot) = %{version}

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust console-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vsock
Summary:        `tracing-subscriber::Layer` for collecting Tokio console telemetry - feature "vsock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-vsock-0.7/default) >= 0.7.2
Requires:       crate(tokio-vsock-0.7/tonic014) >= 0.7.2
Provides:       crate(%{pkgname}/vsock) = %{version}

%description -n %{name}+vsock
This metapackage enables feature "vsock" for the Rust console-subscriber crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
