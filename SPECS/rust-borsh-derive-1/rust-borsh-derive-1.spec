# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name borsh-derive
%global full_version 1.7.0
%global pkgname borsh-derive-1

Name:           rust-borsh-derive-1
Version:        1.7.0
Release:        %autorelease
Summary:        Rust crate "borsh-derive"
License:        Apache-2.0
URL:            https://borsh.io
#!RemoteAsset:  sha256:3ae8fb4fb5740e4b2c4884ff95f5f32f5e8479db1e8fd8eb49ddbe09eb09bb7c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(proc-macro-crate-3/default) >= 3.0.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.81
Requires:       crate(syn-2/fold) >= 2.0.81
Requires:       crate(syn-2/full) >= 2.0.81

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/force-exhaustive-checks) = %{version}
Provides:       crate(%{pkgname}/schema) = %{version}

%description
Source code for takopackized Rust crate "borsh-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
