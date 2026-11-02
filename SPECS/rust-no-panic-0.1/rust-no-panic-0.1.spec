# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name no-panic
%global full_version 0.1.36
%global pkgname no-panic-0.1

Name:           rust-no-panic-0.1
Version:        0.1.36
Release:        %autorelease
Summary:        Rust crate "no-panic"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/no-panic
#!RemoteAsset:  sha256:f967505aabc8af5752d098c34146544a43684817cdba8f9725b292530cabbf53
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.74
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(syn-2/default) >= 2.0.46
Requires:       crate(syn-2/full) >= 2.0.46

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "no-panic"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
