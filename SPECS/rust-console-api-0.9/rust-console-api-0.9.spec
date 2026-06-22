# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name console-api
%global full_version 0.9.0
%global pkgname console-api-0.9

Name:           rust-console-api-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "console-api"
License:        MIT
URL:            https://github.com/tokio-rs/console/blob/main/console-api
#!RemoteAsset:  sha256:e8599749b6667e2f0c910c1d0dff6901163ff698a52d5a39720f61b5be4b20d3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3/default) >= 0.3.31
Requires:       crate(prost-0.14/default) >= 0.14.1
Requires:       crate(prost-types-0.14/default) >= 0.14.1
Requires:       crate(tonic-0.14/codegen) >= 0.14.2
Requires:       crate(tonic-0.14/transport) >= 0.14.2
Requires:       crate(tonic-prost-0.14/default) >= 0.14.2
Requires:       crate(tracing-core-0.1/default) >= 0.1.30
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "console-api"

%package     -n %{name}+transport
Summary:        Protobuf wire format bindings for the Tokio console - feature "transport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.14/codegen) >= 0.14.2
Requires:       crate(tonic-0.14/transport) >= 0.14.2
Provides:       crate(%{pkgname}/transport) = %{version}

%description -n %{name}+transport
This metapackage enables feature "transport" for the Rust console-api crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
