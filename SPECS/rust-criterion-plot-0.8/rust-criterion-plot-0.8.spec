# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name criterion-plot
%global full_version 0.8.2
%global pkgname criterion-plot-0.8

Name:           rust-criterion-plot-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "criterion-plot"
License:        Apache-2.0 OR MIT
URL:            https://github.com/criterion-rs/criterion.rs
#!RemoteAsset:  sha256:d8d80a2f4f5b554395e47b5d8305bc3d27813bacb73493eb1001e8f76dae29ea
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cast-0.3/default) >= 0.3.0
Requires:       crate(itertools-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Criterion's plotting library.
Source code for takopackized Rust crate "criterion-plot"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
