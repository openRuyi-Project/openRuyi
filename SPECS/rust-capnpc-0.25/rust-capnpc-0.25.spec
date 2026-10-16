# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name capnpc
%global full_version 0.25.3
%global pkgname capnpc-0.25

Name:           rust-capnpc-0.25
Version:        0.25.3
Release:        %autorelease
Summary:        Rust crate "capnpc"
License:        MIT
URL:            https://github.com/capnproto/capnproto-rust
#!RemoteAsset:  sha256:fca02be865c8c5a78bfc24b9819006ab6b59bef238467203928e26459557af93
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(capnp-0.25/default) >= 0.25.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "capnpc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
