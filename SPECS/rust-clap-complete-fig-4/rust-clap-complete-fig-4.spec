# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_complete_fig
%global full_version 4.5.2
%global pkgname clap-complete-fig-4

Name:           rust-clap-complete-fig-4
Version:        4.5.2
Release:        %autorelease
Summary:        Rust crate "clap_complete_fig"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:d494102c8ff3951810c72baf96910b980fb065ca5d3101243e6a8dc19747c86b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4/std) >= 4.0.0
Requires:       crate(clap-complete-4/default) >= 4.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clap_complete_fig"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
