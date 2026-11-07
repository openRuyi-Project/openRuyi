# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost
%global full_version 0.9.0
%global pkgname prost-0.9

Name:           rust-prost-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "prost"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:444879275cb4fd84958b1a1d5420d15e6fcf7c235fe47f053c9c2a80aceb6001
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/no-recursion-limit) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "prost"

%package     -n %{name}+default
Summary:        Protocol Buffers implementation for the Rust Language - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/prost-derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust prost crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost-derive
Summary:        Protocol Buffers implementation for the Rust Language - feature "prost-derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-derive-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/prost-derive) = %{version}

%description -n %{name}+prost-derive
This metapackage enables feature "prost-derive" for the Rust prost crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
