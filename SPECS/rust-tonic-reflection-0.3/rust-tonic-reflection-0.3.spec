# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tonic-reflection
%global full_version 0.3.0
%global pkgname tonic-reflection-0.3

Name:           rust-tonic-reflection-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "tonic-reflection"
License:        MIT
URL:            https://github.com/hyperium/tonic
#!RemoteAsset:  sha256:228cc5aa5d3e6e0624b5f756a7558038ee86428d1d58d8c6e551b389b12cf355
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(prost-0.9/default) >= 0.9.0
Requires:       crate(prost-types-0.9/default) >= 0.9.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-stream-0.1/default) >= 0.1.0
Requires:       crate(tokio-stream-0.1/net) >= 0.1.0
Requires:       crate(tonic-0.6/codegen) >= 0.6.0
Requires:       crate(tonic-0.6/default) >= 0.6.0
Requires:       crate(tonic-0.6/prost) >= 0.6.0
Requires:       crate(tonic-build-0.6) >= 0.6.0
Requires:       crate(tonic-build-0.6/prost) >= 0.6.0
Requires:       crate(tonic-build-0.6/transport) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tonic-reflection"

%package     -n %{name}+rustfmt
Summary:        Server Reflection module of `tonic` gRPC implementation - feature "rustfmt" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-build-0.6) >= 0.6.0
Requires:       crate(tonic-build-0.6/prost) >= 0.6.0
Requires:       crate(tonic-build-0.6/rustfmt) >= 0.6.0
Requires:       crate(tonic-build-0.6/transport) >= 0.6.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustfmt) = %{version}

%description -n %{name}+rustfmt
This metapackage enables feature "rustfmt" for the Rust tonic-reflection crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
