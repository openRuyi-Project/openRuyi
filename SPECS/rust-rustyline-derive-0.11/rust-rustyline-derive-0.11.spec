# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustyline-derive
%global full_version 0.11.1
%global pkgname rustyline-derive-0.11

Name:           rust-rustyline-derive-0.11
Version:        0.11.1
Release:        %autorelease
Summary:        Rust crate "rustyline-derive"
License:        MIT
URL:            https://github.com/kkawakam/rustyline
#!RemoteAsset:  sha256:5d66de233f908aebf9cc30ac75ef9103185b4b715c6f2fb7a626aa5e5ede53ab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.86
Requires:       crate(quote-1) >= 1.0.36
Requires:       crate(syn-2/derive) >= 2.0.72
Requires:       crate(syn-2/parsing) >= 2.0.72
Requires:       crate(syn-2/printing) >= 2.0.72
Requires:       crate(syn-2/proc-macro) >= 2.0.72

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustyline-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
