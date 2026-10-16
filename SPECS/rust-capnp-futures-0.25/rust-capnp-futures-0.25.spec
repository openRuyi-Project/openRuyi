# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name capnp-futures
%global full_version 0.25.2
%global pkgname capnp-futures-0.25

Name:           rust-capnp-futures-0.25
Version:        0.25.2
Release:        %autorelease
Summary:        Rust crate "capnp-futures"
License:        MIT
URL:            https://github.com/dwrensha/capnproto-rust
#!RemoteAsset:  sha256:73b69dfddccc57844f9a90f9d72b44b97c326914851ea94fb7da40ef9cad6e8d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(capnp-0.25/default) >= 0.25.0
Requires:       crate(futures-channel-0.3/std) >= 0.3.0
Requires:       crate(futures-util-0.3/io) >= 0.3.0
Requires:       crate(futures-util-0.3/std) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "capnp-futures"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
