# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name axum-core
%global full_version 0.5.5
%global pkgname axum-core-0.5

Name:           rust-axum-core-0.5
Version:        0.5.5
Release:        %autorelease
Summary:        Rust crate "axum-core"
License:        MIT
URL:            https://github.com/tokio-rs/axum
#!RemoteAsset:  sha256:59446ce19cd142f8833f856eb31f3eb097812d1479ab224f54d72428ca21ea22
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.2.0
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(http-body-1/default) >= 1.0.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Requires:       crate(mime-0.3/default) >= 0.3.16
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.7
Requires:       crate(sync-wrapper-1/default) >= 1.0.0
Requires:       crate(tower-layer-0.3/default) >= 0.3.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "axum-core"

%package     -n %{name}+private-docs
Summary:        Core types and traits for axum - feature "__private_docs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-http-0.6/default) >= 0.6.0
Requires:       crate(tower-http-0.6/limit) >= 0.6.0
Provides:       crate(%{pkgname}/private-docs) = %{version}

%description -n %{name}+private-docs
This metapackage enables feature "__private_docs" for the Rust axum-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Core types and traits for axum - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.37
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust axum-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
