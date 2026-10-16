# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vte_generate_state_changes
%global full_version 0.1.2
%global pkgname vte-generate-state-changes-0.1

Name:           rust-vte-generate-state-changes-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "vte_generate_state_changes"
License:        Apache-2.0 OR MIT
URL:            https://github.com/alacritty/vte
#!RemoteAsset:  sha256:2e369bee1b05d510a7b4ed645f5faa90619e05437111783ea5848f28d97d3c2e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.6
Requires:       crate(quote-1/default) >= 1.0.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vte_generate_state_changes"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
