# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name criterion-plot
%global full_version 0.6.0
%global pkgname criterion-plot-0.6

Name:           rust-criterion-plot-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "criterion-plot"
License:        MIT OR Apache-2.0
URL:            https://github.com/bheisler/criterion.rs
#!RemoteAsset:  sha256:9b1bcc0dc7dfae599d84ad0b1a55f80cde8af3725da8313b528da95ef783e338
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cast-0.3/default) >= 0.3.0
Requires:       crate(itertools-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "criterion-plot"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
