# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name capnp-rpc
%global full_version 0.25.1
%global pkgname capnp-rpc-0.25

Name:           rust-capnp-rpc-0.25
Version:        0.25.1
Release:        %autorelease
Summary:        Rust crate "capnp-rpc"
License:        MIT
URL:            https://github.com/capnproto/capnproto-rust
#!RemoteAsset:  sha256:e3c74c337e87f75f3174ffb3513738ab0acc631c04f64cc33b867c60f84771da
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(capnp-0.25/default) >= 0.25.0
Requires:       crate(capnp-futures-0.25/default) >= 0.25.0
Requires:       crate(futures-0.3/std) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "capnp-rpc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
