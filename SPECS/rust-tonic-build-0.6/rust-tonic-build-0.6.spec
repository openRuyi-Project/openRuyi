# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tonic-build
%global full_version 0.6.2
%global pkgname tonic-build-0.6

Name:           rust-tonic-build-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "tonic-build"
License:        MIT
URL:            https://github.com/hyperium/tonic
#!RemoteAsset:  sha256:9403f1bafde247186684b230dc6f38b5cd514584e8bec1dd32514be4745fa757
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compression) = %{version}
Provides:       crate(%{pkgname}/rustfmt) = %{version}
Provides:       crate(%{pkgname}/transport) = %{version}

%description
Source code for takopackized Rust crate "tonic-build"

%package     -n %{name}+default
Summary:        Codegen module of `tonic` gRPC implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/prost) = %{version}
Requires:       crate(%{pkgname}/rustfmt) = %{version}
Requires:       crate(%{pkgname}/transport) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tonic-build crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost-build
Summary:        Codegen module of `tonic` gRPC implementation - feature "prost-build" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-build-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/prost) = %{version}
Provides:       crate(%{pkgname}/prost-build) = %{version}

%description -n %{name}+prost-build
This metapackage enables feature "prost-build" for the Rust tonic-build crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "prost" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
