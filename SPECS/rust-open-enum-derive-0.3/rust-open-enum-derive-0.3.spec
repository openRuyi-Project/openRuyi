# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name      open-enum-derive
%global full_version    0.3.0
%global pkgname         open-enum-derive-0.3

Name:           rust-open-enum-derive-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "open-enum-derive"
License:        Apache-2.0
URL:            https://github.com/kupiakos/open-enum/tree/main/derive
#!RemoteAsset:  sha256:894ae443e59fecf7173ab3b963473f44193fa71b3c8953c61a5bd5f30880bb88
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/repr-c) = %{version}

Requires:       crate(proc-macro2-1/default) >= 1.0.43
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0
Requires:       crate(syn-1/full) >= 1.0.0

%description
Source code for takopackized Rust crate "open-enum-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
