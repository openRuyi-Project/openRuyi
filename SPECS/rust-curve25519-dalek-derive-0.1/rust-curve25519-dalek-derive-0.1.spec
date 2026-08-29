# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name curve25519-dalek-derive
%global full_version 0.1.1
%global pkgname curve25519-dalek-derive-0.1

Name:           rust-curve25519-dalek-derive-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "curve25519-dalek-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/dalek-cryptography/curve25519-dalek
#!RemoteAsset:  sha256:f46882e17999c6cc590af592290432be3bce0428cb0d5f8b6715e4dc7b383eb3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.66
Requires:       crate(quote-1/default) >= 1.0.31
Requires:       crate(syn-2/default) >= 2.0.27
Requires:       crate(syn-2/full) >= 2.0.27
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "curve25519-dalek-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
