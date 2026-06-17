# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pnet_transport
%global full_version 0.35.0
%global pkgname pnet-transport-0.35

Name:           rust-pnet-transport-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "pnet_transport"
License:        MIT OR Apache-2.0
URL:            https://github.com/libpnet/libpnet
#!RemoteAsset:  sha256:5f604d98bc2a6591cf719b58d3203fd882bdd6bf1db696c4ac97978e9f4776bf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.147
Requires:       crate(pnet-base-0.35) >= 0.35.0
Requires:       crate(pnet-packet-0.35/default) >= 0.35.0
Requires:       crate(pnet-sys-0.35/default) >= 0.35.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pnet_transport"

%package     -n %{name}+std
Summary:        Cross-platform, transport layer networking - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-base-0.35/std) >= 0.35.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pnet_transport crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
