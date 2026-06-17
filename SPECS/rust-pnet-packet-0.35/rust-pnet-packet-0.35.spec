# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pnet_packet
%global full_version 0.35.0
%global pkgname pnet-packet-0.35

Name:           rust-pnet-packet-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "pnet_packet"
License:        MIT OR Apache-2.0
URL:            https://github.com/libpnet/libpnet
#!RemoteAsset:  sha256:4c96ebadfab635fcc23036ba30a7d33a80c39e8461b8bd7dc7bb186acb96560f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glob-0.3) >= 0.3.1
Requires:       crate(pnet-base-0.35) >= 0.35.0
Requires:       crate(pnet-macros-0.35/default) >= 0.35.0
Requires:       crate(pnet-macros-support-0.35/default) >= 0.35.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pnet_packet"

%package     -n %{name}+std
Summary:        Cross-platform, binary packet parsing and manipulation - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-base-0.35/std) >= 0.35.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pnet_packet crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
